Name:       wp-cli
Version:    1.4.1
Release:    1%{?dist}
Summary:    The command line interface for WordPress
License:    MIT
URL:        http://wp-cli.org/
Source0:    wp-cli-1.4.1.phar
Source1:    wp.1
BuildArch:  noarch


%post
echo "PHP 5.3.29 or above must be installed."

%description
WP-CLI is the command-line interface for WordPress.
You can update plugins, configure multisite installs
and much more, without using a web browser.

%prep
wget -nv -O %{SOURCE0} "https://github.com/wp-cli/wp-cli/releases/download/v1.4.1/wp-cli-1.4.1.phar"
chmod +x %{SOURCE0}
{
    echo '.TH "WP" "1"'
    php %{SOURCE0} --help
} \
    | sed -e 's/^\([A-Z ]\+\)$/.SH "\1"/' \
    | sed -e 's/^  wp$/wp \\- The command line interface for WordPress/' \
    > %{SOURCE1}
%build

%install
mkdir -p %{buildroot}%{_bindir}
cp -a %{SOURCE0} %{buildroot}%{_bindir}/wp
mkdir -p %{buildroot}%{_mandir}/man1
cp -a %{SOURCE1} %{buildroot}%{_mandir}/man1/

%files
%attr(0755, root, root) %{_bindir}/wp
%attr(0644, root, root) %{_mandir}/man1/wp.1*

%changelog
* Tue Dec 12 2017 Murtaza Sarıaltun <murtaza.sarialtun@ozguryazzilim.com.tr> - 1.4.1-1
- Update version 1.4.1
- Remove php requirements.
- Update creating man page steps.
- Added output message. 

* Fri Jul 7 2017 Murtaza Sarıaltun <murtaza.sarialtun@ozguryazilim.com.tr> - 1.2.1-1
- First release of the spec file
- Check the spec file with `rpmlint -i -v wp-cli-rpm.spec`
- Build the package with `rpmbuild -bb wp-cli-rpm.spec`
