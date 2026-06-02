# Codesigning and Notarization

## macOS

To distribute a `.app` outside the Mac App Store, it must be codesigned with a Developer ID certificate and notarized by Apple.

**What you need:**

- An [Apple Developer account](https://developer.apple.com/) ($99/year)
- A **Developer ID Application** certificate installed in your Keychain
- An app-specific password for your Apple ID (create one at [appleid.apple.com](https://appleid.apple.com) under Sign-In & Security → App-Specific Passwords)
- Xcode command-line tools (`xcode-select --install`)

**Set your signing credentials** — either export these before running make, or edit the defaults at the top of `Makefile`:

```shell
export SIGNING_ID="Developer ID Application: Your Name (TEAMID)"
export APPLE_ID="you@example.com"
export APP_PASSWORD="@keychain:AC_PASSWORD"   # or the password directly
export TEAM_ID="YOURTEAMID"
```

Storing the app-specific password in Keychain is recommended:
```shell
xcrun notarytool store-credentials AC_PASSWORD \
  --apple-id you@example.com \
  --team-id YOURTEAMID \
  --password <app-specific-password>
```

**Run the full pipeline:**

```shell
make dist       # build → codesign → notarize → staple
```

Or step by step:

```shell
make build-mac       # PyInstaller freeze
make codesign-mac    # codesign with hardened runtime + entitlements
make notarize-mac    # submit to Apple, wait, staple ticket
```

Notarization can take a few minutes. The `--wait` flag in the Makefile blocks until Apple returns a result.

## Windows — Azure Trusted Signing

Windows executables are signed using [Azure Trusted Signing](https://learn.microsoft.com/en-us/azure/trusted-signing/). Signing runs automatically in CI on releases, but can also be done locally.

**What you need:**

- An [Azure Trusted Signing](https://learn.microsoft.com/en-us/azure/trusted-signing/quickstart) account and certificate profile ($10/month)
- An Azure service principal (app registration) with the **Trusted Signing Certificate Profile Signer** role
- [AzureSignTool](https://github.com/vcsjones/AzureSignTool) installed locally (requires .NET):
  ```shell
  dotnet tool install -g AzureSignTool
  ```

**Set your credentials** as environment variables (or in CI secrets):

```shell
export AZURE_TENANT_ID="your-tenant-id"
export AZURE_CLIENT_ID="your-client-id"
export AZURE_CLIENT_SECRET="your-client-secret"
# These default to the thingm-signing account/profile — override if different:
export AZURE_ENDPOINT="https://wus2.codesigning.azure.net/"
export AZURE_ACCOUNT="thingm-signing"
export AZURE_CERT_PROFILE="ThingMProfile"
```

**Run locally:**

```shell
make dist-win    # build → sign
# or step by step:
make build-win
make sign-win
```

**In GitHub Actions**, signing is handled by the `azure/trusted-signing-action` step, triggered on releases or manual dispatch. The required secrets are `AZURE_TENANT_ID`, `AZURE_CLIENT_ID`, and `AZURE_CLIENT_SECRET`.
