{ pkgs ? import <nixpkgs> { } }:
with pkgs;
mkShell {
  buildInputs = [
    python3Full
    pylint
    black
  ];

  shellHook = ''
  '';
}
