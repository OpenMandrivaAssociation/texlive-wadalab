%global tl_name wadalab
%global tl_revision 42428

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	3
Summary:	Wadalab (Japanese) font packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/wadalab
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wadalab.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/wadalab.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
These are font bundles for the Japanese Wadalab fonts which work with
the CJK package. All subfonts now have glyph names compliant to the
Adobe Glyph List, making ToUnicode CMaps in PDF documents (created
automatically by dvipdfmx) work correctly. All font bundles now contain
virtual Unicode subfonts.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from wadalab:
Map dgj.map
Map dmj.map
Map mc2j.map
Map mcj.map
Map mr2j.map
Map mrj.map
TL_DROPIN_EOF
echo '%dir %{_texmf_updmap_d}' >> %{specpartsdir}/%{name}.files.specpart
echo '%{_texmf_updmap_d}/%{tl_name}' >> %{specpartsdir}/%{name}.files.specpart
