# BYD Android Localized

[English](README.md) · [العربية](README.ar.md) · [Русский](README.ru.md)

**BYD Android 9.16.1 · 2026 年 9 月更新**

BYD Android 多语言版公开更新。可下载 APK 或访问下载页面。

[**下载 APK**](https://github.com/shihabal3amri/BYD-Android/releases/download/v9.16.1-20260914/BYD-Android_9.16.1_20260914.apk) · [BYD Android 多语言版 · 下载](https://shihabal3amri.github.io/BYD-Android/zh-Hans/) · [报告问题](https://github.com/shihabal3amri/BYD-Android/issues/new?template=bug-report.yml)

## 本次更新内容

- BYD 9.16.1 支持英语、阿拉伯语、俄语、西班牙语和简体中文原文模式。
- 支持签名翻译包，手动更新独立可用，自动更新默认关闭。完全关闭并重新打开 BYD 后生效。
- 重新设计翻译面板，优化阿拉伯语从右到左布局，并按所选语言显示上次检查时间。
- 修正验证码重发等翻译，同时保留现有靠近解锁和摄像头功能。
- 保留距离校准、可选离开上锁和自定义标签，不改变靠近解锁功能版本。

## 应用界面

<a href="assets/dashboard.jpg"><img src="assets/dashboard.jpg" alt="带蓝牙控制项的车辆页面" width="190"></a>
<a href="assets/walkup-setup.jpg"><img src="assets/walkup-setup.jpg" alt="靠近解锁、后台检测和距离校准设置" width="190"></a>
<a href="assets/settings.jpg"><img src="assets/settings.jpg" alt="语言、底部标签栏和靠近解锁设置" width="190"></a>
<a href="assets/profile.jpg"><img src="assets/profile.jpg" alt="BYD 个人资料和车辆卡片" width="190"></a>

## 1. 安装或更新

1. 在 Android 手机上下载 APK 并打开文件。
2. 若 Android 提示，请允许当前浏览器或文件管理器安装应用，然后按照安装器提示操作。
3. 打开 BYD 并登录自己的账户。在我的 → 设置中选择语言和底部标签。

更新本项目兼容版本时，请保留现有应用并覆盖安装，以保留本地设置。本版本沿用项目签名密钥；仍可能需要重新登录。

如果使用原版 BYD 应用，请先卸载，因为签名不同。卸载会删除本地数据，可能需要重新登录并设置蓝牙钥匙。

## 2. 设置靠近解锁

1. 确认现有 BYD 蓝牙钥匙能够手动上锁和解锁。
2. 打开我的 → 设置 → 靠近解锁并启用。允许访问附近设备，保持蓝牙开启。
3. 打开后台检测，按钥匙类型完成设置。支持的固定地址钥匙使用 Android 的一次性车辆检测设置；地址变化的钥匙使用广播检测。
4. 点击校准距离，按日常携带方式放置手机，测量解锁和上锁位置并保存。
5. 如需自动上锁，启用离开时上锁。在保持就绪中设置手机的后台活动权限。

仍可使用手动阈值。校准期间会暂停自动指令。口袋和周围环境会影响信号强度，它不是以米为单位的精确距离。

## 兼容性与反馈

需要 64 位 ARM Android 手机。新增蓝牙检测使用 Android 8 及以上 API；Companion 检测需要 Android 12 及以上且设备支持。自动解锁需要可正常使用的 BYD 蓝牙钥匙。

西班牙语仍在审校。部分动态内容和图片仍为中文。后台表现及车辆功能因手机和车型而异。强制停止后请重新打开 BYD 以恢复检测。摄像头启动仍依赖车辆和 BYD 服务。

反馈时请提供手机、Android 版本、车型、应用版本及复现步骤。请先移除截图或日志中的账户信息、车架号和位置。

## 下载与校验

[更新说明与校验值](https://github.com/shihabal3amri/BYD-Android/releases/tag/v9.16.1-20260914) · [release.json](release.json)

`BYD-Android_9.16.1_20260914.apk` · 375,288,531 bytes

SHA-256: `b41484116028f751774d51f42f108be7aed39afd136f22bfa324026d587beca1`

## 维护此下载页面

Update `release.json` and `content/*.json`, then run:

```sh
python scripts/build_site.py
python scripts/validate_site.py
```

APK downloads belong in GitHub Releases. This repository contains the download
page, screenshots, instructions and issue templates. It does not contain the
original BYD app source, signing keys, user logs or account data.

本项目为非官方项目，与比亚迪无隶属关系，也未获得其认可。原版应用及资源属于各自所有者。
