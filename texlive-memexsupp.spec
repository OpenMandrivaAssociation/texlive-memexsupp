Name:		texlive-memexsupp
Version:	15878
Release:	2
Summary:	Experimental memoir support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/memexsupp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memexsupp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memexsupp.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package of code proposed as supporting material for memoir.
The package is intended as a test bed for such code, which may
in the fullness of time be adopted into the main memoir
release.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/memexsupp/memexsupp.sty
%doc %{_texmfdistdir}/doc/latex/memexsupp/README
%doc %{_texmfdistdir}/doc/latex/memexsupp/memexsupp.pdf
%doc %{_texmfdistdir}/doc/latex/memexsupp/memexsupp.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
