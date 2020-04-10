# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device ido
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi 3

%define installable_zip 1
%define droid_target_aarch64 1

%define straggler_files \
/plat_file_contexts\
/plat_hwservice_contexts\
/plat_property_contexts\
/plat_seapp_contexts\
/plat_service_contexts\
/vendor_file_contexts\
/vendor_hwservice_contexts\
/vendor_property_contexts\
/vendor_seapp_contexts\
/vendor_service_contexts\
/vndservice_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc
