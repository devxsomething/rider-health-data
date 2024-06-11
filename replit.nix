{pkgs}: {
  deps = [
    pkgs.python311Packages.clvm-tools
    pkgs.pkg-config
    pkgs.libffi
    pkgs.cacert
    pkgs.rustc
    pkgs.libiconv
    pkgs.cargo
  ];
}
