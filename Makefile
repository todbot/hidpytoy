APP_NAME     = HIDPyToy
APP_VERSION  = 0.1.0
ENTITLEMENTS = entitlements.plist
SPEC_FILE    = HIDPyToy.spec

APPLE_SIGNING_ID   ?= Developer ID Application: Your Name (TEAMID)
APPLE_ID           ?= your@apple.id
APPLE_APP_PASSWORD ?= @keychain:AC_PASSWORD
APPLE_TEAM_ID      ?= YOURTEAMID
# APPLE_CERTIFICATE and APPLE_CERTIFICATE_PASSWORD are also required in CI
# (base64-encoded .p12 and its password) but are not used here — local builds
# assume the certificate is already installed in the macOS Keychain.

# Azure Trusted Signing (Windows) — set via environment or CI secrets
AZURE_ENDPOINT    ?= https://wus2.codesigning.azure.net/
AZURE_ACCOUNT     ?= thingm-signing
AZURE_CERT_PROFILE ?= ThingMProfile
AZURE_TENANT_ID   ?=
AZURE_CLIENT_ID   ?=
AZURE_CLIENT_SECRET ?=

HIDTOYWINDOW_PY = src/main/python/HIDToyWindow.py
HIDTOYWINDOW_UI = src/main/python/HIDToyWindow.ui

.PHONY: all run regen-ui build-mac build-win build-linux codesign-mac notarize-mac sign-win dist-win dist clean help

all: $(HIDTOYWINDOW_PY)

$(HIDTOYWINDOW_PY): $(HIDTOYWINDOW_UI)
	pyside6-uic $< -o $@

regen-ui: $(HIDTOYWINDOW_PY)  ## Regenerate HIDToyWindow.py from HIDToyWindow.ui

run: $(HIDTOYWINDOW_PY)  ## Run in development mode
	python src/main/python/main.py

build-mac:  ## Build standalone .app (macOS)
	pyinstaller --clean --noconfirm $(SPEC_FILE)

build-win:  ## Build standalone .exe (Windows)
	pyinstaller --clean --noconfirm $(SPEC_FILE)

build-linux:  ## Build standalone binary (Linux)
	pyinstaller --clean --noconfirm $(SPEC_FILE)

codesign-mac: build-mac  ## Build and codesign .app (macOS)
	codesign --deep --force --options runtime \
	  --entitlements $(ENTITLEMENTS) \
	  --sign "$(APPLE_SIGNING_ID)" \
	  dist/$(APP_NAME).app

notarize-mac: codesign-mac  ## Build, codesign, and notarize .app (macOS)
	ditto -c -k --keepParent dist/$(APP_NAME).app dist/$(APP_NAME)-$(APP_VERSION).zip
	xcrun notarytool submit dist/$(APP_NAME)-$(APP_VERSION).zip \
	  --apple-id "$(APPLE_ID)" --password "$(APPLE_APP_PASSWORD)" \
	  --team-id "$(APPLE_TEAM_ID)" --wait
	xcrun stapler staple dist/$(APP_NAME).app

sign-win: build-win  ## Build and sign .exe via Azure Trusted Signing (Windows)
	AzureSignTool sign \
	  --azure-key-vault-url "$(AZURE_ENDPOINT)" \
	  --azure-key-vault-tenant-id "$(AZURE_TENANT_ID)" \
	  --azure-key-vault-client-id "$(AZURE_CLIENT_ID)" \
	  --azure-key-vault-client-secret "$(AZURE_CLIENT_SECRET)" \
	  --trusted-signing-account-name "$(AZURE_ACCOUNT)" \
	  --trusted-signing-certificate-profile-name "$(AZURE_CERT_PROFILE)" \
	  --timestamp-rfc3161 "http://timestamp.acs.microsoft.com" \
	  dist/$(APP_NAME)/$(APP_NAME).exe

dist-win: sign-win  ## Build, sign, and package .exe (Windows)

dist: notarize-mac  ## Build, codesign, notarize, and package .app (macOS)

clean:  ## Remove build artifacts
	rm -rf dist/ build/
	rm -rf src/main/python/__pycache__
	rm -f $(APP_NAME)-$(APP_VERSION).zip

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-16s %s\n", $$1, $$2}'
