# generated by cabal-rpm-2.1.0 --standalone
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global ghc_without_dynamic 1
%global ghc_without_shared 1
%undefine with_ghc_prof
%undefine with_haddock
%global without_prof 1
%global without_haddock 1
%global debug_package %{nil}

%global pkg_name ghcup
%global pkgver %{pkg_name}-%{version}

Name:           %{pkg_name}
Version:        0.1.18.0
Release:        2%{?dist}
Summary:        Ghc toolchain installer

License:        LGPLv3+
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources
# missing from tarball
Source1:        dirutils.h
Patch0:         ghcup-default-flags.patch
Patch1:         ghcup-0.1.18.0-cabal-dirutils.h.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HsOpenSSL-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-brick-devel
BuildRequires:  ghc-bytestring-devel
#BuildRequires:  ghc-bz2-devel
BuildRequires:  ghc-cabal-plan-devel
BuildRequires:  ghc-case-insensitive-devel
#BuildRequires:  ghc-casing-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptohash-sha256-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-disk-free-space-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
#BuildRequires:  ghc-haskus-utils-types-devel
#BuildRequires:  ghc-haskus-utils-variant-devel
#BuildRequires:  ghc-http-io-streams-devel
BuildRequires:  ghc-io-streams-devel
#BuildRequires:  ghc-libarchive-devel
#BuildRequires:  ghc-lzma-static-devel
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-mtl-devel
#BuildRequires:  ghc-optics-devel
BuildRequires:  ghc-optparse-applicative-devel
#BuildRequires:  ghc-os-release-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-terminal-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-regex-posix-devel
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-retry-devel
BuildRequires:  ghc-safe-devel
BuildRequires:  ghc-safe-exceptions-devel
BuildRequires:  ghc-split-devel
#BuildRequires:  ghc-streamly-devel
#BuildRequires:  ghc-strict-base-devel
BuildRequires:  ghc-tagsoup-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-temporary-devel
#BuildRequires:  ghc-terminal-progress-bar-devel
BuildRequires:  ghc-terminal-size-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
#BuildRequires:  ghc-unix-bytestring-devel
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-uri-bytestring-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-devel
#BuildRequires:  ghc-versions-devel
BuildRequires:  ghc-vty-devel
BuildRequires:  ghc-word8-devel
#BuildRequires:  ghc-yaml-streamly-devel
BuildRequires:  ghc-zlib-devel
BuildRequires:  cabal-install > 1.18
# for missing dep 'haskus-utils-variant':
#BuildRequires:  ghc-haskus-utils-data-devel
# for missing dep 'http-io-streams':
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-blaze-builder-devel
#BuildRequires:  ghc-brotli-streams-devel
BuildRequires:  ghc-cryptohash-sha1-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-openssl-streams-devel
#BuildRequires:  ghc-xor-devel
# for missing dep 'libarchive':
#BuildRequires:  ghc-chs-cabal-devel
#BuildRequires:  ghc-composition-prelude-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-unix-compat-devel
# for missing dep 'optics':
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-optics-core-devel
#BuildRequires:  ghc-optics-extra-devel
#BuildRequires:  ghc-optics-th-devel
# for missing dep 'streamly':
#BuildRequires:  ghc-atomic-primops-devel
#BuildRequires:  ghc-fusion-plugin-types-devel
BuildRequires:  ghc-heaps-devel
#BuildRequires:  ghc-lockfree-queue-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-transformers-base-devel
# for missing dep 'versions':
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-parser-combinators-devel
# for missing dep 'yaml-streamly':
BuildRequires:  ghc-attoparsec-devel
#BuildRequires:  ghc-libyaml-streamly-devel
BuildRequires:  ghc-scientific-devel
# End cabal-rpm deps
# for libarchive
BuildRequires: libarchive-devel
# for brotli
BuildRequires: brotli-devel

%description
A rewrite of the shell script ghcup, for providing a more stable user
experience and exposing an API.


%prep
# Begin cabal-rpm setup:
%setup -q
# End cabal-rpm setup
cp %SOURCE1 cbits/
%patch0 -p1 -b .orig
%patch1 -p1 -b .orig


%build
# Begin cabal-rpm build:
%global cabal_install %{_bindir}/cabal
%cabal_install update
%if 0%{?rhel} && 0%{?rhel} < 9
%cabal_install sandbox init
%cabal_install install
%endif
# End cabal-rpm build


%install
# Begin cabal-rpm install
mkdir -p %{buildroot}%{_bindir}
%if 0%{?fedora} >= 33 || 0%{?rhel} > 8
%if 0%{?fedora} >= 36
%ghc_set_gcc_flags
%endif
%cabal_install install --install-method=copy --enable-executable-stripping --installdir=%{buildroot}%{_bindir} --constraint="libarchive +system-libarchive" --constraint="streamly +use-unliftio"
%else
for i in .cabal-sandbox/bin/*; do
strip -s -o %{buildroot}%{_bindir}/$(basename $i) $i
done
%endif
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions/
%{buildroot}%{_bindir}/%{name} --bash-completion-script %{name} | sed s/filenames/default/ > %{buildroot}%{_datadir}/bash-completion/completions/%{name}
# End cabal-rpm install


%files
# Begin cabal-rpm files:
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
# End cabal-rpm files


%changelog
* Mon Nov 21 2022 Jens Petersen <petersen@redhat.com> - 0.1.18.0-2
- enable tui and internal-downloader

* Mon Nov 21 2022 Jens Petersen <petersen@redhat.com> - 0.1.18.0-1
- initial package
