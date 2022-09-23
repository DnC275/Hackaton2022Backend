{
  description = "Python with mach-nix template";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:nixos/nixpkgs/nixos-22.05";

    pypi-deps-db = {
      url = "github:DavHau/pypi-deps-db";
      inputs.nixpkgs.follows = "nixpkgs";
      inputs.mach-nix.follows = "mach-nix";
    };
    mach-nix = {
      url = "github:DavHau/mach-nix/3.5.0";
      inputs.nixpkgs.follows = "nixpkgs";
      inputs.pypi-deps-db.follows = "pypi-deps-db";
    };
  };

  outputs = { self, nixpkgs, flake-utils, mach-nix, ... }:
    flake-utils.lib.eachDefaultSystem
      (system:
        let
          pkgs = nixpkgs.legacyPackages.${system};
          machNix = mach-nix.lib.${system};
        in
          {
            devShell = pkgs.mkShell {
              buildInputs = with pkgs; [
                (machNix.mkPython {
                  python = "python37";
                  requirements = builtins.readFile ./requirements.txt;
                })

                ffmpeg

                pyright
                black
              ];
            };
          }
      );
}
