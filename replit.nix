{pkgs}: {
  deps = [
    pkgs.pkg-config
    pkgs.libffi
    pkgs.cacert
    pkgs.rustc
    pkgs.libiconv
    pkgs.cargo
  ];
}
