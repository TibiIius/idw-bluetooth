{ pkgs ? import <nixpkgs> { } }:
with pkgs;
mkShell {
  buildInputs = [
    python3Full
  ];

  shellHook = ''
  '';
}