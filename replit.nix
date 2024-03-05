{pkgs}: {
  deps = [
    pkgs.firefox-esr-102-unwrapped
    pkgs.ungoogled-chromium
    pkgs.chromedriver
    pkgs.geckodriver
  ];
}
