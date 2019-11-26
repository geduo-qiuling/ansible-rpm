Name:nginx		
Version:1.10.3
Release:10
Summary:nginx is a web server software	
Group:nginx
License:GPL	
URL:www.test.com	
Source0:nginx-1.10.3.tar.gz

#BuildRequires:	
#Requires:	

%description
nginx [engine x] is an HTTP and reverse proxy server

%post
useradd web
echo "[Unit]
Description=The NGINX HTTP Server
After=network.target remote-fs.target nss-lookup.target

[Service]
Type=forking
ExecStart=/usr/local/nginx/sbin/nginx
ExecReload=/usr/local/nginx/sbin/nginx -s reload
ExecStop=/usr/bin/killall -9 nginx

[Install]
WantedBy=multi-user.target" > /usr/lib/systemd/system/nginx.service

%prep
%setup -q


%build
./configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc
/usr/local/nginx/*


%changelog

