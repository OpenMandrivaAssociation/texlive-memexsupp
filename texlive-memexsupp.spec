# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/memexsupp
# catalog-date 2008-08-22 15:19:59 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-memexsupp
Version:	0.1
Release:	1
Summary:	Experimental memoir support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/memexsupp
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memexsupp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/memexsupp.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A package of code proposed as supporting material for memoir.
The package is intended as a test bed for such code, which may
in the fullness of time be adopted into the main memoir
release.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/memexsupp/memexsupp.sty
%doc %{_texmfdistdir}/doc/latex/memexsupp/README
%doc %{_texmfdistdir}/doc/latex/memexsupp/memexsupp.pdf
%doc %{_texmfdistdir}/doc/latex/memexsupp/memexsupp.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
