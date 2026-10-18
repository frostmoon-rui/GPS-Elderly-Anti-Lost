# GPS Elderly Location Assistant

An educational App Inventor project, version 6.1.9.
The screen and blocks are translated into English. Embedded contact numbers have
been cleared; configure your own contact before testing calls or SMS.

## Source

- `source/gps-location-assistant.aia`: importable project archive.
- `source/src/`: editable screen JSON wrapper and Blockly XML.
- `source/youngandroidproject/project.properties`: project settings.
- `source/assets/compass.png`: a newly generated compass diagram.

The loose files mirror the archive contents. Rebuild the AIA after editing them;
importing the AIA does not read loose files from this repository.

## Features represented in the blocks

The screen displays longitude, latitude, altitude, speed, GPS status, orientation,
and a pedometer count. It saves a reference location and radius using TinyDB,
compares location changes with configured thresholds, and includes phone-call and
SMS components. Orientation updates rotate the compass sprite.

## Setup and original interaction flow

1. Import `source/gps-location-assistant.aia` into a compatible App Inventor editor.
   The project uses legacy component versions; review any migration prompts.
2. Review the Designer and Blocks before building. The original startup message
   names Funtouch OS and Android 8.1.0; current Android compatibility is unverified.
3. Build your own APK in the editor. On a test device, review permissions needed
   for location, calls, and SMS. Calls and SMS need suitable device/SIM support
   and may incur charges.
4. Enter a radius in meters before GPS acquires a signal. The original flow uses
   a default of 1000 meters and warns against settings below 10 meters.
5. On first use, follow the prompt to restart after a GPS signal is available.
   Enter and save a contact number. The original blocks include long-press editing
   and one-change restrictions; review these before using the contact controls.

This is an unvalidated educational prototype. Its coordinate-threshold comparison
is not a verified distance calculation or reliable geofence. GPS accuracy,
background execution, permissions, and notification delivery depend on the device.
Do not rely on it for emergency response or a person's safety.

## Cleanup and validation

The repository contains source rather than prebuilt APKs, duplicate videos,
competition appendices, screenshots, and unreviewed office/PDF documents. Obsolete
internal backups and bundled images of uncertain provenance were omitted. No
license grant for the original project is inferred from this cleanup.

Offline validation checks archive integrity, XML/JSON parsing, component and asset
references, English text, cleared contact defaults, and archive/source consistency.
No APK was executed, app launched, call placed, or SMS sent. Import/build/device
testing is still required.

Run the repeatable offline checks with Python 3:

```sh
python -m unittest discover -s tests -q
```
