# Tagging Automation QA Pro

A desktop tool built with Python, Tkinter, and Playwright to automate the QA process for website tagging and element presence. It allows users to manage URLs, define keywords, run automated tests, and generate Excel reports with embedded screenshots.

---

## English Instructions

### Key Features
- **URL Management**: Easily add, remove, and manage a list of URLs for testing.
- **Automated Testing**: Run a "Fast Test" to automatically browse through all URLs, search for specified keywords, and capture screenshots upon discovery.
- **Manual Browser Control**: Manually launch and control a browser for detailed inspection.
- **Screenshot Capture**: Take full-page screenshots or combined shots of the browser and the application GUI.
- **Excel Reporting**: Generate comprehensive `.xlsx` reports detailing test results, including the URL, keyword found, status, and embedded screenshots for visual verification.
- **Customizable Workspace**: Change the default directory where all session files, logs, screenshots, and reports are stored.

### Important: macOS First-Time Setup

Due to macOS's security features, you **must** grant the application specific permissions to function correctly. The system will prompt you when a permission is first needed. Please click **"Allow"**.

If you accidentally deny the permissions, or if the app fails to save files or take screenshots, you need to grant them manually:

1.  Open **System Settings**.
2.  Go to **Privacy & Security**.
3.  Find and click on the following sections:
    - **Files and Folders**: Find `Tag QA Tool` in the list, and ensure it has permission to access your **Documents Folder** and **Pictures Folder**. This is required to save reports, logs, and screenshots.
    - **Screen Recording**: Find `Tag QA Tool` and turn on the switch. This is absolutely necessary for the app to take any screenshots.

---
---

## 中文说明

### 核心功能
- **URL 管理**: 轻松添加、删除和管理用于测试的 URL 列表。
- **自动化测试**: 运行“Fast Test”模式，程序将自动访问所有 URL，搜索指定的关键字，并在发现时捕获屏幕截图。
- **手动浏览器控制**: 手动启动并控制一个浏览器，用于精细化的检查和调试。
- **屏幕截图**: 支持截取完整的浏览器页面，或将浏览器与软件界面合并截图。
- **Excel 报告生成**: 生成图文并茂的 `.xlsx` 格式测试报告，包含 URL、发现的关键字、测试状态，并嵌入了截图证据。
- **自定义工作目录**: 可以自由更改所有会话、日志、截图和报告文件的存储位置。

### 重要：macOS 首次运行设置

由于 macOS 的安全机制，你**必须**授予本应用特定权限才能使其正常工作。当应用首次需要某项权限时，系统会自动弹出请求对话框，请务必点击 **“允许”**。

如果你不小心拒绝了权限，或发现应用无法保存文件、无法截图，你需要手动开启权限：

1.  打开 **“系统设置”**。
2.  进入 **“隐私与安全性”**。
3.  在右侧列表中找到并点击以下项目：
    - **文件和文件夹**: 在列表中找到 `Tag QA Tool`，确保它有权访问你的 **“文稿文件夹”** 和 **“图片文件夹”**。这是保存报告、日志和截图所必需的。
    - **屏幕录制**: 在列表中找到 `Tag QA Tool` 并**打开**开关。这是应用进行任何截图操作的绝对必要条件。
