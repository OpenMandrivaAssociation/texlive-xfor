Name:		texlive-xfor
Version:	15878
Release:	2
Summary:	A reimplimentation of the LaTeX for-loop macro
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xfor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xfor.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xfor.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xfor.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package redefines the LaTeX internal \@for macro so that
the loop may be prematurely terminated. The action is akin to
the C/Java break statement, except that the loop does not
terminate until the end of the current iteration.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/xfor/xfor.sty
%doc %{_texmfdistdir}/doc/latex/xfor/CHANGES
%doc %{_texmfdistdir}/doc/latex/xfor/README
%doc %{_texmfdistdir}/doc/latex/xfor/sample.tex
%doc %{_texmfdistdir}/doc/latex/xfor/xfor.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xfor/xfor.dtx
%doc %{_texmfdistdir}/source/latex/xfor/xfor.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
