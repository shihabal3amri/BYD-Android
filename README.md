# BYD Android Localized

[English](README.md) · [العربية](README.ar.md) · [Русский](README.ru.md)

**BYD Android 9.16.1 · September 2026 Update**

Public release of the localized BYD Android app. Download the APK below or use the download page.

[**Download APK**](https://github.com/shihabal3amri/BYD-Android/releases/download/v9.16.1-20260914/BYD-Android_9.16.1_20260914.apk) · [BYD Android Localized · Download](https://shihabal3amri.github.io/BYD-Android/) · [Report a problem](https://github.com/shihabal3amri/BYD-Android/issues/new?template=bug-report.yml)

## What’s in this release

- English, Arabic, Russian, Spanish and original-text Simplified Chinese mode.
- Signed translation packs with independent manual downloads; automatic updates default off. Fully close and reopen BYD to apply.
- Redesigned Translations panel with proper Arabic RTL layout and last-check timestamps in the selected language.
- Translation fixes including OTP resend messages, while preserving existing Walk-up, Bluetooth and Surround View behavior.
- Distance calibration, optional walk-away locking and bottom-tab customization retained; the Walk-up feature version is unchanged.

## Inside the app

<a href="assets/dashboard.jpg"><img src="assets/dashboard.jpg" alt="My Vehicle dashboard with Bluetooth controls" width="190"></a>
<a href="assets/walkup-setup.jpg"><img src="assets/walkup-setup.jpg" alt="Walk-up unlock settings with background detection, distance calibration and manual thresholds" width="190"></a>
<a href="assets/settings.jpg"><img src="assets/settings.jpg" alt="Settings with Language, Bottom bar and Walk-up unlock entries" width="190"></a>
<a href="assets/profile.jpg"><img src="assets/profile.jpg" alt="BYD profile page and vehicle card" width="190"></a>

## 1. Install or update

1. Download the APK on your Android phone and open the downloaded file.
2. If Android asks, allow this browser or file manager to install apps, then follow the installer.
3. Open BYD and sign in to your own account. Go to Me → Settings to choose your language and bottom tabs.

Updating a compatible project build? Keep the app and install over it to retain local settings. This release uses the same signing key. You may need to sign in again.

Using the original BYD app? Uninstall it before installing this APK because the signing keys differ. Uninstalling removes its local data; you may need to sign in and set up your Bluetooth key again.

## 2. Set up Walk-up unlock

1. Confirm that your existing BYD Bluetooth key can lock and unlock your car manually.
2. Open Me → Settings → Walk-up unlock and enable the feature. Allow nearby-device access and keep Bluetooth on.
3. Open Background detection and follow the instructions for your key. Supported fixed-address keys use Android’s one-time car detection setup; keys with changing addresses use broadcast detection.
4. Tap Calibrate distances. Measure your unlock and lock positions with the phone where you normally carry it, then save.
5. Enable Lock when walking away if you want automatic locking. Use Keep it ready for your phone’s background activity settings.

Manual thresholds remain available. Calibration pauses automatic commands. Signal strength varies with pockets and surroundings; it measures signal, not an exact distance in metres.

## Compatibility & feedback

Use a 64-bit ARM Android phone. The added Bluetooth detection uses Android 8+ APIs; Android Companion detection requires Android 12+ and device support. A working BYD Bluetooth key is required for automatic unlocking.

Spanish remains a draft. Some live content and artwork remain Chinese. Background behavior and available features vary by phone and car. Reopen BYD after force-stopping it to resume detection. Camera startup depends on the vehicle and BYD service.

Something not working? Include your phone, Android version, car model, app version and steps to reproduce. Remove account details, VINs and locations from screenshots or logs.

## Downloads and verification

[Release notes & checksums](https://github.com/shihabal3amri/BYD-Android/releases/tag/v9.16.1-20260914) · [release.json](release.json)

`BYD-Android_9.16.1_20260914.apk` · 375,288,531 bytes

SHA-256: `b41484116028f751774d51f42f108be7aed39afd136f22bfa324026d587beca1`

## Maintaining this download page

Update `release.json` and `content/*.json`, then run:

```sh
python scripts/build_site.py
python scripts/validate_site.py
```

APK downloads belong in GitHub Releases. This repository contains the download
page, screenshots, instructions and issue templates. It does not contain the
original BYD app source, signing keys, user logs or account data.

Unofficial project, not affiliated with or endorsed by BYD. BYD’s original application and assets belong to their respective owners.
