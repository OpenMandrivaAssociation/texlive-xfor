# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xfor
# catalog-date 2009-02-05 23:18:07 +0100
# catalog-license lppl
# catalog-version 1.05
Name:		texlive-xfor
Version:	1.05
Release:	1
Summary:	A reimplimentation of the LaTeX for-loop macro
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xfor
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xfor.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xfor.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xfor.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package redefines the LaTeX internal \@for macro so that
the loop may be prematurely terminated. The action is akin to
the C/Java break statement, except that the loop does not
terminate until the end of the current iteration.

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
%{_texmfdistdir}/tex/latex/xfor/xfor.sty
%doc %{_texmfdistdir}/doc/latex/xfor/CHANGES
%doc %{_texmfdistdir}/doc/latex/xfor/README
%doc %{_texmfdistdir}/doc/latex/xfor/sample.tex
%doc %{_texmfdistdir}/doc/latex/xfor/xfor.pdf
#- source
%doc %{_texmfdistdir}/source/latex/xfor/xfor.dtx
%doc %{_texmfdistdir}/source/latex/xfor/xfor.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
