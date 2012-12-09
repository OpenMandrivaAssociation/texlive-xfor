# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/xfor
# catalog-date 2009-02-05 23:18:07 +0100
# catalog-license lppl
# catalog-version 1.05
Name:		texlive-xfor
Version:	1.05
Release:	2
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.05-2
+ Revision: 757646
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.05-1
+ Revision: 719936
- texlive-xfor
- texlive-xfor
- texlive-xfor

