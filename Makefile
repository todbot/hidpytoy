APP_NAME     = HIDPyToy
APP_VERSION  = 0.1.0

SIGNING_ID   ?= Developer ID Application: Tod Kurt (K3Y8NR25XK)
APPLE_ID     ?= your@apple.id
APP_PASSWORD ?= @keychain:AC_PASSWORD
TEAM_ID      ?= YOURTEAMID

# Azure Trusted Signing (Windows) — set via environment or CI secrets
AZURE_ENDPOINT     ?= https://wus2.codesigning.azure.net/
AZURE_ACCOUNT      ?= thingm-signing
AZURE_CERT_PROFILE ?= ThingMProfile
AZURE_TENANT_ID    ?=
AZURE_CLIENT_ID    ?=
AZURE_CLIENT_SECRET ?=

HIDTOYWINDOW_PY = src/hidpytoy/HIDToyWindow.py
HIDTOYWINDOW_UI = src/hidpytoy/HIDToyWindow.ui

.PHONY: all run regen-ui build-mac build-win build-linux \
        package-mac package-mac-dev sign-win package-win dist clean

all: $(HIDTOYWINDOW_PY)

$(HIDTOYWINDOW_PY): $(HIDTOYWINDOW_UI)
	pyside6-uic $< -o $@

regen-ui: $(HIDTOYWINDOW_PY)

run: $(HIDTOYWINDOW_PY)
	PYTHONPATH=src python -m hidpytoy

build-mac: $(HIDTOYWINDOW_PY)
	briefcase build macOS

build-win: $(HIDTOYWINDOW_PY)
	briefcase build windows

build-linux: $(HIDTOYWINDOW_PY)
	briefcase build linux

# macOS: ad-hoc sign only, no notarization — runs on this machine only
package-mac-dev: build-mac
	briefcase package macOS --adhoc-sign

# macOS: sign + notarize + DMG in one step
# Notarization credentials must be pre-stored in keychain:
#   xcrun notarytool store-credentials briefcase-macOS-TEAMID --apple-id ... --password ... --team-id ...
package-mac: build-mac
	briefcase package macOS --identity "$(SIGNING_ID)"

# Windows: sign exe with Azure Trusted Signing, then package as MSI
sign-win: build-win
	AzureSignTool sign \
	  --azure-key-vault-url "$(AZURE_ENDPOINT)" \
	  --azure-key-vault-tenant-id "$(AZURE_TENANT_ID)" \
	  --azure-key-vault-client-id "$(AZURE_CLIENT_ID)" \
	  --azure-key-vault-client-secret "$(AZURE_CLIENT_SECRET)" \
	  --trusted-signing-account-name "$(AZURE_ACCOUNT)" \
	  --trusted-signing-certificate-profile-name "$(AZURE_CERT_PROFILE)" \
	  --timestamp-rfc3161 "http://timestamp.acs.microsoft.com" \
	  build/$(APP_NAME)/windows/app/$(APP_NAME).exe

package-win: sign-win
	briefcase package windows

dist: package-mac

clean:
	rm -rf build/ dist/
	rm -rf src/hidpytoy/__pycache__
	rm -f $(HIDTOYWINDOW_PY)
