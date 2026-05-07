# Protodesk

<p align="center">
  <img src="./assets/logo.png" alt="Logo" width="200" height="200"/>
</p>

<p align="center">Unofficial desktop app for Proton</p>

<p align="center">
  <img src="./scrshots/showcase.gif" alt="Screenshots"/>
</p>

## About

**Protodesk** is a free open‑source desktop app for Proton. It brings together Proton Mail, Proton Calendar and Proton Drive into a single Linux application.

## Features

- **Easy to set up** – Download the AppImage, make it executable and start using Protodesk.
- **Session persistence** – Session data is stored on disk.
- **File downloads** – Attachments from Proton Mail and files from Proton Drive can be downloaded.
- **Proton Mail, Calendar and Drive integration** – All three core services are available from one UI.
- **Open‑source** – The source code is available for inspection.

## Download

Only Linux is supported (AppImage). The AppImage can be downloaded from the releases page.

<p align="center">
  <a href="https://github.com/YourName/protodesk/releases/download/v1.4.0/Protodesk-1.4.0-x86_64.AppImage">
    <img src="./assets/download.png" alt="Download AppImage" height="75"/>
  </a>
</p>

## Contributions

We welcome contributions. Fork the repository, create a branch, make changes, commit with a clear message and open a PR.

## Donations

If you would like to support development, use any of the following:

<p align="center">
  <a href="https://www.paypal.com/donate/?hosted_button_id=8KU8MDWA86SNJ">
    <img alt="Paypal" src="./assets/paypal.svg" width="170"/>
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://ko-fi.com/YourName">
    <img alt="Ko-fi" src="https://ko-fi.com/img/githubbutton_sm.svg" width="350"/>
  </a>
</p>

## Packaging & Distribution

The app is built as an AppImage on Linux. The CI workflow in `.github/workflows/cd.yml` runs on every push to `main`.

To build locally:

```bash
pip install -r requirements.txt
python -m PyInstaller --onefile --add-data "assets;assets" --add-data "scrshots;scrshots" app.py
appimagetool ./dist/Protodesk-1.4.0-x86_64.AppImage
```

## Developers & Maintainers

YourName – [yourname@yourdomain.com](mailto:yourname@yourdomain.com)
