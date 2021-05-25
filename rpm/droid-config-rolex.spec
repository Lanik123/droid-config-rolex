# Reference: ../droid-configs-device/droid-configs.inc

%define device rolex
%define vendor xiaomi

%define vendor_pretty Xiaomi
%define device_pretty Redmi 4A

%define community_adaptation 1
%define pixel_ratio 1.5

# Device-specific ofono configuration
Provides: ofono-configs
Obsoletes: ofono-configs-mer

%include droid-configs-device/droid-configs.inc
%include patterns/patterns-sailfish-device-adaptation-rolex.inc
%include patterns/patterns-sailfish-device-configuration-rolex.inc
