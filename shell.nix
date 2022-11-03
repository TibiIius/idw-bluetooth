{ pkgs ? import <nixpkgs> { } }:

let
  my-python = pkgs.python3;
  python-with-my-packages = my-python.withPackages (p: with p; [
    pylint
    black
    pydbus
  ]);
in
pkgs.mkShell {
  buildInputs = [
    python-with-my-packages
    pkgs.python310Packages.pydbus
  ];
  shellHook = ''
    PYTHONPATH=${python-with-my-packages}/${python-with-my-packages.sitePackages}
  '';
}
