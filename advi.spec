%define name	advi
%define version	1.6.0
%define release	%mkrel 4

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	LGPL
Summary:	Programmable DVI previewer for slides written in LaTeX
Group:		Publishing
URL:		http://pauillac.inria.fr/advi
Source:		ftp://ftp.inria.fr/INRIA/Projects/cristal/advi/%{name}-%{version}.tar.bz2
Patch0:		active-dvi-1.6.0-warn-error.patch
BuildRequires:	ocaml
BuildRequires:	ocaml-camlimages-devel >= 2.20
BuildRequires:	ocaml-labltk
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	tetex-latex
BuildRequires:	tetex-dvips
BuildRequires:	hevea
BuildRequires:  png-devel
Requires(post):	tetex
Requires(postun): tetex
BuildRoot: 	%{_tmppath}/%{name}-buildroot

%description 
To preview DVI files, Active-DVI features:

    * Color anti-aliasing.
    * Inclusion of images (via the Camlimages package) with alpha channel and
      blending.
    * Encapsulated Postscript File inclusion (using graphics macros package).
    * Gpic specials to display pictures.
    * Correct treatment of many (but not all) inlined-Postscript specials.
    * Page background settings.
    * Japanese pTeX DVI extension support (screen shot). 

To present your DVI files, Active-DVI features:

    * Basic effects for presentation (pause, delay, dynamic text color change).
    * Annotations displayed on demand (similar to pop-up balloons).
    * Hyper links from slide to slide or to other files (including DVI files).
    * Replay of previously recorded parts of the display.
    * Text movements.
    * Page transitions.
    * Embedded applications (launched and killed on demand from within. the
      presentation text source), with precise security policy.
    * Scratching on slide to interactively modify the text on screen. 

Active-DVI special effects are set and launched from within your LaTeX source
file via the macros of the advi.sty LaTeX package provided by the distribution.

In addition, Caml hackers can program new and fancy Active-DVI effects in the
source code of the presenter.

%prep
%setup -q
%patch0 -p2
find . -type d -name CVS | xargs rm -rf
find . -type f -name ".*" | xargs rm -f
rm -f doc/index.html
sed -i -e "s/resize_window/resize_subwindow/" grY11.c

%build
%configure2_5x
%make
# remove empty file
rm -f doc/splash.out

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{name}
install -m 755 advi.opt $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 644 doc/{scratch_write_,scratch_draw_,}splash.dvi tex/* $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p %{_bindir}/mktexlsr

%postun -p %{_bindir}/mktexlsr

%files
%defattr(-,root,root)
%doc Announce COPYING INDEX INSTALL LGPL README TODO doc
%{_bindir}/%{name}
%{_datadir}/texmf/tex/latex/%{name}

