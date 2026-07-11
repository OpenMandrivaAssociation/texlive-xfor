%global tl_name xfor
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.05
Release:	%{tl_revision}.1
Summary:	A reimplementation of the LaTeX for-loop macro
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xfor
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xfor.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xfor.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xfor.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package redefines the LaTeX internal \@for macro so that the loop
may be prematurely terminated. The action is akin to the C/Java break
statement, except that the loop does not terminate until the end of the
current iteration

