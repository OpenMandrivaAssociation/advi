Summary:	Programmable DVI previewer for slides written in LaTeX
Name:		advi
Version:	1.10.2
Release:	2
License:	LGPLv2.1+
Group:		Publishing
Url:		http://advi.inria.fr/
Source:		http://advi.inria.fr/%{name}-%{version}.tar.gz
Patch0:		advi-1.10.2-dont-make-doc.patch
Patch1:		advi-1.10.2-manpage.patch
Patch2:		advi-1.10.2-no-local-advirc.patch
Patch3:		advi-1.10.2-typo-message.patch
Patch4:		advi-1.10.2-automake.patch
BuildRequires:	ghostscript
BuildRequires:	hevea
BuildRequires:	imagemagick
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	ocaml-labltk
BuildRequires:	tetex-dvips
BuildRequires:	tetex-latex
BuildRequires:	texlive-kpathsea
BuildRequires:	ocaml-camlimages-devel >= 4.0
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xinerama)
Requires:	ghostscript
Requires:	hevea
Requires:	imagemagick
Requires(post,postun):	texlive-kpathsea

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

%files
%doc COPYING LGPL README TODO doc
%{_bindir}/%{name}
%{_bindir}/%{name}.byt
%{_libdir}/ocaml/stublibs/dll%{name}.so
%{_datadir}/texmf/tex/latex/%{name}/
%{_mandir}/man1/%{name}.1*

%post -p %{_bindir}/mktexlsr

%postun -p %{_bindir}/mktexlsr

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
rm -f doc/index.html

mkdir m4
cp *.m4 m4/

%build
autoreconf
%configure2_5x
make

%install
%makeinstall_std

# To avoid "E: unstripped-binary-or-object"
chmod 0755 %{buildroot}%{_libdir}/ocaml/stublibs/dll%{name}.so

