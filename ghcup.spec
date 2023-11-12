# generated by cabal-rpm-2.1.5 --standalone
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
Version:        0.1.20.0
Release:        1%{?dist}
Summary:        Ghc toolchain installer

License:        LGPL-3.0-only
Url:            https://hackage.haskell.org/package/%{name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources
Patch0:         ghcup-default-flags.patch

# Begin cabal-rpm deps:
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-binary-devel
%if %{defined fedora}
BuildRequires:  ghc-brick-devel
%endif
BuildRequires:  ghc-bytestring-devel
#BuildRequires:  ghc-bz2-devel
#BuildRequires:  ghc-cabal-install-parsers-devel
%if %{defined fedora} && 0%{?fedora} < 38
BuildRequires:  ghc-cabal-plan-devel
%endif
BuildRequires:  ghc-case-insensitive-devel
#BuildRequires:  ghc-casing-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-cryptohash-sha256-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-directory-devel
%if %{defined fedora}
BuildRequires:  ghc-disk-free-space-devel
%endif
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
#BuildRequires:  ghc-haskus-utils-types-devel
#BuildRequires:  ghc-haskus-utils-variant-devel
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
%if %{defined fedora}
BuildRequires:  ghc-retry-devel
%endif
BuildRequires:  ghc-safe-devel
%if %{defined fedora}
BuildRequires:  ghc-safe-exceptions-devel
%endif
BuildRequires:  ghc-split-devel
#BuildRequires:  ghc-streamly-devel
#BuildRequires:  ghc-strict-base-devel
BuildRequires:  ghc-tagsoup-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-terminal-size-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unix-devel
#BuildRequires:  ghc-unix-bytestring-devel
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-unordered-containers-devel
%if %{defined fedora}
BuildRequires:  ghc-uri-bytestring-devel
%endif
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-vector-devel
#BuildRequires:  ghc-versions-devel
%if %{defined fedora}
BuildRequires:  ghc-vty-devel
BuildRequires:  ghc-word8-devel
%endif
#BuildRequires:  ghc-yaml-streamly-devel
BuildRequires:  ghc-zlib-devel
BuildRequires:  cabal-install > 1.18
# for missing dep 'atomic-primops':
BuildRequires:  ghc-primitive-devel
# for missing dep 'binary-instances':
%if %{defined fedora}
BuildRequires:  ghc-binary-orphans-devel
%endif
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-time-compat-devel
%if %{defined fedora}
BuildRequires:  ghc-vector-binary-instances-devel
%endif
# for missing dep 'cabal-install-parsers':
%if 0%{?fedora} >= 39
BuildRequires:  ghc-Cabal-syntax-devel
%endif
BuildRequires:  ghc-lukko-devel
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-tar-devel
# for missing dep 'cabal-plan':
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-parsec-devel
%if %{defined fedora}
BuildRequires:  ghc-semialign-devel
BuildRequires:  ghc-singleton-bool-devel
%endif
BuildRequires:  ghc-these-devel
# for missing dep 'chs-deps':
BuildRequires:  ghc-array-devel
# for missing dep 'libarchive':
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-unix-compat-devel
# for missing dep 'lockfree-queue':
%if %{defined fedora}
BuildRequires:  ghc-abstract-deque-devel
%endif
# for missing dep 'optics':
BuildRequires:  ghc-array-devel
%if %{defined fedora} && 0%{?fedora} < 38
BuildRequires:  ghc-optics-core-devel
%endif
# for missing dep 'optics-core':
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-indexed-traversable-devel
# for missing dep 'optics-extra':
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-hashable-devel
%if 0%{?fedora} >= 38
BuildRequires:  ghc-indexed-traversable-instances-devel
%endif
# for missing dep 'optics-th':
BuildRequires:  ghc-th-abstraction-devel
# for missing dep 'recursion-schemes':
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-data-fix-devel
%if %{defined fedora}
BuildRequires:  ghc-free-devel
%endif
BuildRequires:  ghc-th-abstraction-devel
# for missing dep 'streamly':
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-heaps-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-transformers-base-devel
%if 0%{?fedora} > 38
BuildRequires:  ghc-unicode-data-devel
%endif
# for missing dep 'streamly-core':
BuildRequires:  ghc-heaps-devel
BuildRequires:  ghc-monad-control-devel
# for missing dep 'topograph':
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base-orphans-devel
# for missing dep 'versions':
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-parser-combinators-devel
# for missing dep 'yaml-streamly':
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-scientific-devel
# End cabal-rpm deps
# for text2
BuildRequires:  gcc-c++
# for libarchive
BuildRequires:  libarchive-devel
%if %{defined el9}
BuildRequires:  ghc-terminfo-devel
%endif

%description
A rewrite of the shell script ghcup, for providing a more stable user
experience and exposing an API.


%prep
# Begin cabal-rpm setup:
%autosetup -p1
# End cabal-rpm setup


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
%if 0%{?fedora} || 0%{?rhel} >= 9
%ghc_set_gcc_flags
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
* Sun Nov 12 2023 Jens Petersen <petersen@redhat.com> - 0.1.20.0-1
- https://hackage.haskell.org/package/ghcup-0.1.20.0/changelog

* Fri Apr  7 2023 Jens Petersen <petersen@redhat.com> - 0.1.19.2-1
- https://hackage.haskell.org/package/ghcup-0.1.19.2/changelog
- disable internal-downloader

* Mon Nov 21 2022 Jens Petersen <petersen@redhat.com> - 0.1.18.0-2
- enable tui and internal-downloader

* Mon Nov 21 2022 Jens Petersen <petersen@redhat.com> - 0.1.18.0-1
- initial package
