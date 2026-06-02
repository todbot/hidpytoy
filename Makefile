APP_NAME     = HIDPyToy
APP_VERSION  = 0.1.0
ENTITLEMENTS = entitlements.plist
SPEC_FILE    = HIDPyToy.spec

SIGNING_ID   ?= Developer ID Application: Your Name (TEAMID)
APPLE_ID     ?= your@apple.id
APP_PASSWORD ?= @keychain:AC_PASSWORD
TEAM_ID      ?= YOURTEAMID

# Azure Trusted Signing (Windows) — set via environment or CI secrets
AZURE_ENDPOINT    ?= https://wus2.codesigning.azure.net/
AZURE_ACCOUNT     ?= thingm-signing
AZURE_CERT_PROFILE ?= ThingMProfile
AZURE_TENANT_ID   ?=
AZURE_CLIENT_ID   ?=
AZURE_CLIENT_SECRET ?=

HIDTOYWINDOW_PY = src/main/python/HIDToyWindow.py
HIDTOYWINDOW_UI = src/main/python/HIDToyWindow.ui

.PHONY: all run regen-ui build-mac build-win build-linux codesign-mac notarize-mac sign-win dist-win dist clean

all: $(HIDTOYWINDOW_PY)

$(HIDTOYWINDOW_PY): $(HIDTOYWINDOW_UI)
	pyside6-uic $< -o $@

regen-ui: $(HIDTOYWINDOW_PY)

run: $(HIDTOYWINDOW_PY)
	python src/main/python/main.py

build-mac:
	pyinstaller --clean --noconfirm $(SPEC_FILE)

build-win:
	pyinstaller --clean --noconfirm $(SPEC_FILE)

build-linux:
	pyinstaller --clean --noconfirm $(SPEC_FILE)

codesign-mac: build-mac
	codesign --deep --force --options runtime \
	  --entitlements $(ENTITLEMENTS) \
	  --sign "$(SIGNING_ID)" \
	  dist/$(APP_NAME).app

notarize-mac: codesign-mac
	ditto -c -k --keepParent dist/$(APP_NAME).app dist/$(APP_NAME)-$(APP_VERSION).zip
	xcrun notarytool submit dist/$(APP_NAME)-$(APP_VERSION).zip \
	  --apple-id "$(APPLE_ID)" --password "$(APP_PASSWORD)" \
	  --team-id "$(TEAM_ID)" --wait
	xcrun stapler staple dist/$(APP_NAME).app

sign-win: build-win
	AzureSignTool sign \
	  --azure-key-vault-url "$(AZURE_ENDPOINT)" \
	  --azure-key-vault-tenant-id "$(AZURE_TENANT_ID)" \
	  --azure-key-vault-client-id "$(AZURE_CLIENT_ID)" \
	  --azure-key-vault-client-secret "$(AZURE_CLIENT_SECRET)" \
	  --trusted-signing-account-name "$(AZURE_ACCOUNT)" \
	  --trusted-signing-certificate-profile-name "$(AZURE_CERT_PROFILE)" \
	  --timestamp-rfc3161 "http://timestamp.acs.microsoft.com" \
	  dist/$(APP_NAME)/$(APP_NAME).exe

dist-win: sign-win

dist: notarize-mac

clean:
	rm -rf dist/ build/
	rm -rf src/main/python/__pycache__
	rm -f src/main/python/HIDToyWindow.py
	rm -f $(APP_NAME)-$(APP_VERSION).zip
