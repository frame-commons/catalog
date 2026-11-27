# Steam Frame community software catalog

Public source code for the Valve Steam Frame, sorted by the piece of the headset each project
provides. The catalog rebuilds itself every week from GitHub. It lists what we have found so far,
not everything that exists: see "Getting listed" below.

- **[catalog.json](catalog.json)** is the same list as data, for installers, launchers and
  other lists to read. Use it freely.
- **[GUIDE.md](GUIDE.md)** is the field guide: for each part of the headset, the open tools worth
  installing first, the alternatives and their limits.
- **[COMPAT.md](COMPAT.md)** shows which projects were tested on which headset update.
- **[spec/steam-frame-yml.md](spec/steam-frame-yml.md)** describes `steam-frame.yml`, a small
  optional file a project keeps in its own repo to describe itself.

## Related

[awesome-steam-frame](https://github.com/kosantosbik/awesome-steam-frame) is the hand-kept list most people know,
and its links seeded this catalog. It covers games and hardware more widely; this catalog adds data,
manifests and compatibility records.

## Getting listed

Any one of these works. None of them makes your project part of frame-commons or asks
anything of you.

1. Add the GitHub topic `steam-frame` to your repository. It shows up under "Not sorted yet"
   at the next weekly build.
2. Add a [`steam-frame.yml`](spec/steam-frame-yml.md) to your repository root. Two lines are
   enough, and the catalog then files you under the right sections and keeps your entry
   current. Add `tested:` records and you appear in [COMPAT.md](COMPAT.md).
3. Open a pull request adding a line to [data/projects.yml](data/projects.yml), for your own
   project or someone else's.

To be left out, open an issue or a pull request adding your repo to
[data/excluded.yml](data/excluded.yml).

## The catalog

Descriptions are our one-line summaries or the repository's own GitHub description; if one is
wrong, a pull request to [data/projects.yml](data/projects.yml) fixes it. A project that provides several
pieces appears in each section. "none found" in the Licence column means the repo has no licence file,
so its code is public but not open source until its author adds one.

<!-- catalog:start -->
### Camera access (5)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [Frametop/frametop](https://github.com/Frametop/frametop) | Multi-screen KDE Plasma desktop, 3D mouse and gaze input; ships ft-camd (tracking-camera frames into a shared-memory ring) and camera hand… | headset | MIT | 428 | 2026-11-26 |  |
| [Curtis-VL/FrameEyeCameraFeed](https://github.com/Curtis-VL/FrameEyeCameraFeed) | Eye-camera feeds for EyeTrackVR | headset | MIT | 18 | 2026-10-02 |  |
| [Sippbox/frame-passthrough-pip](https://github.com/Sippbox/frame-passthrough-pip) | Passthrough camera as a picture-in-picture panel |  | MIT | 2 | 2026-10-22 |  |
| [danthedaniel/roommate-radar](https://github.com/danthedaniel/roommate-radar) | Highlights people nearby using the tracking cameras and object detection |  | AGPL-3.0 | 1 | 2026-11-07 |  |
| [MrDarkMoon/phone-screen](https://github.com/MrDarkMoon/phone-screen) | Tracks a real phone with the tracking cameras and shows it in VR |  | MIT | 1 | 2026-11-19 |  |

### Hands (2)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [Frametop/frametop](https://github.com/Frametop/frametop) | Multi-screen KDE Plasma desktop, 3D mouse and gaze input; ships ft-camd (tracking-camera frames into a shared-memory ring) and camera hand… | headset | MIT | 428 | 2026-11-26 |  |
| [spyjacob/steam-frame-hand-tracking](https://github.com/spyjacob/steam-frame-hand-tracking) | Optical hand tracking for PC streaming |  | MIT | 18 | 2026-11-12 |  |

### Eyes (8)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [Frametop/frametop](https://github.com/Frametop/frametop) | Multi-screen KDE Plasma desktop, 3D mouse and gaze input; ships ft-camd (tracking-camera frames into a shared-memory ring) and camera hand… | headset | MIT | 428 | 2026-11-26 |  |
| [sasaken1102r/frameeyeosc](https://github.com/sasaken1102r/frameeyeosc) | frameeyeosc fork: gaze, eyelids, pupils over OSC, LiveLink and a VRCFT module |  | MIT | 154 | 2026-11-26 |  |
| [konsti219/frameeyeosc](https://github.com/konsti219/frameeyeosc) (archived) | Eye-tracking data over OSC |  | MIT | 76 | 2026-11-13 |  |
| [Project-Babble/Babble-Frame-Runtime](https://github.com/Project-Babble/Babble-Frame-Runtime) | Eye and mouth expressions on the headset, into VRCFaceTracking | headset | GPL-3.0 | 72 | 2026-11-23 |  |
| [Curtis-VL/FrameEyeCameraFeed](https://github.com/Curtis-VL/FrameEyeCameraFeed) | Eye-camera feeds for EyeTrackVR | headset | MIT | 18 | 2026-10-02 |  |
| [hakumaguro/vrcft-steam-frame](https://github.com/hakumaguro/vrcft-steam-frame) | VRCFaceTracking module with a tuning tool |  | MIT | 14 | 2026-11-11 |  |
| [huntergcook/SquintThru](https://github.com/huntergcook/SquintThru) | Squint to toggle passthrough |  | none found | 8 | 2026-10-30 |  |
| [miyu0-bit/frameeye-helper](https://github.com/miyu0-bit/frameeye-helper) | Installer for frameeyeosc |  | MIT | 6 | 2026-09-30 |  |

### Face (4)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [sasaken1102r/frameeyeosc](https://github.com/sasaken1102r/frameeyeosc) | frameeyeosc fork: gaze, eyelids, pupils over OSC, LiveLink and a VRCFT module |  | MIT | 154 | 2026-11-26 |  |
| [Project-Babble/Babble-Frame-Runtime](https://github.com/Project-Babble/Babble-Frame-Runtime) | Eye and mouth expressions on the headset, into VRCFaceTracking | headset | GPL-3.0 | 72 | 2026-11-23 |  |
| [hakumaguro/vrcft-steam-frame](https://github.com/hakumaguro/vrcft-steam-frame) | VRCFaceTracking module with a tuning tool |  | MIT | 14 | 2026-11-11 |  |
| [SteffanDonal/SRanipatch](https://github.com/SteffanDonal/SRanipatch) | Unofficial SRanipal runtime for the VIVE Facial Tracker &amp; VRCFT on Windows and Steam Frame | both | none found | 4 | 2026-11-17 | yes |

### Passthrough (9)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [KominoVR/frame-passthrough-shortcuts](https://github.com/KominoVR/frame-passthrough-shortcuts) | Controller shortcuts for passthrough, including the colour camera module |  | MIT | 30 | 2026-11-04 |  |
| [VioletTides/KnockThru](https://github.com/VioletTides/KnockThru) | Double-knock to toggle passthrough |  | MIT | 30 | 2026-11-10 |  |
| [bod09/frame-autopass](https://github.com/bod09/frame-autopass) | Switches between colour and IR passthrough automatically |  | MIT | 27 | 2026-10-06 |  |
| [thunderheronight/splat-workshop](https://github.com/thunderheronight/splat-workshop) | Turns colour-camera recordings into Gaussian splats |  | GPL-3.0 | 14 | 2026-10-28 |  |
| [spyjacob/steam-frame-chroma-key](https://github.com/spyjacob/steam-frame-chroma-key) | Chroma-key mixed reality for PC streaming |  | MIT | 10 | 2026-10-11 |  |
| [huntergcook/SquintThru](https://github.com/huntergcook/SquintThru) | Squint to toggle passthrough |  | none found | 8 | 2026-10-30 |  |
| [AstronautCheetah/frame-tweaks](https://github.com/AstronautCheetah/frame-tweaks) | Tweak installer | headset | MIT | 5 | 2026-11-26 | yes |
| [Sippbox/frame-passthrough-pip](https://github.com/Sippbox/frame-passthrough-pip) | Passthrough camera as a picture-in-picture panel |  | MIT | 2 | 2026-10-22 |  |
| [danthedaniel/roommate-radar](https://github.com/danthedaniel/roommate-radar) | Highlights people nearby using the tracking cameras and object detection |  | AGPL-3.0 | 1 | 2026-11-07 |  |

### Streaming (10)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [WiVRn/WiVRn](https://github.com/WiVRn/WiVRn) | OpenXR streaming from a Linux PC | both | GPL-3.0 | 1882 | 2026-11-25 |  |
| [demonixis/oxrsys](https://github.com/demonixis/oxrsys) | OpenXR runtime for macOS; its Steam Frame client is an open draft PR (#30) | pc | MPL-2.0 | 129 | 2026-11-04 |  |
| [simplysanatori/moonlight-xr-steam-frame](https://github.com/simplysanatori/moonlight-xr-steam-frame) | Native Moonlight game-streaming client | headset | GPL-3.0 | 29 | 2026-11-25 |  |
| [xhuytox/scrcpy4Frame](https://github.com/xhuytox/scrcpy4Frame) | Android phone mirroring in VR |  | MIT | 27 | 2026-11-08 |  |
| [arealjim/frame-stream](https://github.com/arealjim/frame-stream) | Streams macOS OpenXR apps to the Frame | both | MIT | 12 | 2026-11-03 |  |
| [spyjacob/steam-frame-chroma-key](https://github.com/spyjacob/steam-frame-chroma-key) | Chroma-key mixed reality for PC streaming |  | MIT | 10 | 2026-10-11 |  |
| [simplysanatori/moonlight-xr-lepton](https://github.com/simplysanatori/moonlight-xr-lepton) | Moonlight XR via Lepton |  | GPL-3.0 | 9 | 2026-11-06 |  |
| [AstronautCheetah/frame-tweaks](https://github.com/AstronautCheetah/frame-tweaks) | Tweak installer | headset | MIT | 5 | 2026-11-26 | yes |
| [marcus-universe/frame-audio-mixer](https://github.com/marcus-universe/frame-audio-mixer) | Mixes the microphone for PC streaming and standalone apps |  | MIT | 5 | 2026-11-14 |  |
| [nickgkg/FrameCast](https://github.com/nickgkg/FrameCast) | Casts the headset view to a Chromecast, with sound | headset | MIT | 2 | 2026-11-09 |  |

### Input (16)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [Frametop/frametop](https://github.com/Frametop/frametop) | Multi-screen KDE Plasma desktop, 3D mouse and gaze input; ships ft-camd (tracking-camera frames into a shared-memory ring) and camera hand… | headset | MIT | 428 | 2026-11-26 |  |
| [CreoleVR/QuestLHSync](https://github.com/CreoleVR/QuestLHSync) | Aligns Lighthouse trackers and controllers to the Frame's tracking |  | MIT | 285 | 2026-11-01 |  |
| [baketnk/frame-yap](https://github.com/baketnk/frame-yap) | Voice typing on the headset | headset | MIT | 31 | 2026-11-03 |  |
| [KominoVR/frame-passthrough-shortcuts](https://github.com/KominoVR/frame-passthrough-shortcuts) | Controller shortcuts for passthrough, including the colour camera module |  | MIT | 30 | 2026-11-04 |  |
| [khvn26/steam-frame-dictation](https://github.com/khvn26/steam-frame-dictation) | Offline dictation |  | MIT | 26 | 2026-10-28 |  |
| [Rulez777/FramePicoTracker](https://github.com/Rulez777/FramePicoTracker) | Research on using PICO body trackers with the Frame |  | none found | 20 | 2026-11-11 |  |
| [techieyann/frame-voice](https://github.com/techieyann/frame-voice) | Controller-triggered voice input |  | MIT | 15 | 2026-10-07 |  |
| [sasaken1102r/frame-aux-shortcuts](https://github.com/sasaken1102r/frame-aux-shortcuts) | Shortcuts on the auxiliary buttons |  | MIT | 10 | 2026-10-17 |  |
| [juanramosjr1/frame-voice](https://github.com/juanramosjr1/frame-voice) | Voice input with copy and paste |  | MIT | 7 | 2026-10-08 |  |
| [sasaken1102r/frame-jp-keyboard](https://github.com/sasaken1102r/frame-jp-keyboard) | Japanese flick keyboard |  | MIT | 7 | 2026-11-03 |  |
| [Andalu30/frame-unboundedMouse-vibed](https://github.com/Andalu30/frame-unboundedMouse-vibed) | A mouse drives the laser pointer |  | MIT | 5 | 2026-11-21 |  |
| [AstronautCheetah/frame-tweaks](https://github.com/AstronautCheetah/frame-tweaks) | Tweak installer | headset | MIT | 5 | 2026-11-26 | yes |
| [groffta/whisper-frame](https://github.com/groffta/whisper-frame) | Push-to-talk Whisper dictation |  | MIT | 4 | 2026-10-07 |  |
| [uxandy/frame-input](https://github.com/uxandy/frame-input) | Shares keyboard and mouse with a Windows PC |  | MIT | 1 | 2026-10-26 |  |
| [MichaelScottsman/nso-frame-bridge](https://github.com/MichaelScottsman/nso-frame-bridge) | Nintendo Switch Online GameCube controller over Bluetooth |  | Apache-2.0 | 0 | 2026-10-17 |  |
| [PhoenixSheppy/lhctl](https://github.com/PhoenixSheppy/lhctl) | Control your SteamVR Base Stations 2.0 directly from your Steam Frame over Bluetooth | headset | MIT | 0 | 2026-11-26 | yes |

### Voice (8)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [sasaken1102r/frame-mic-tuner](https://github.com/sasaken1102r/frame-mic-tuner) | Microphone echo and noise settings panel |  | MIT | 63 | 2026-11-22 |  |
| [baketnk/frame-yap](https://github.com/baketnk/frame-yap) | Voice typing on the headset | headset | MIT | 31 | 2026-11-03 |  |
| [khvn26/steam-frame-dictation](https://github.com/khvn26/steam-frame-dictation) | Offline dictation |  | MIT | 26 | 2026-10-28 |  |
| [techieyann/frame-voice](https://github.com/techieyann/frame-voice) | Controller-triggered voice input |  | MIT | 15 | 2026-10-07 |  |
| [juanramosjr1/frame-voice](https://github.com/juanramosjr1/frame-voice) | Voice input with copy and paste |  | MIT | 7 | 2026-10-08 |  |
| [AstronautCheetah/frame-tweaks](https://github.com/AstronautCheetah/frame-tweaks) | Tweak installer | headset | MIT | 5 | 2026-11-26 | yes |
| [marcus-universe/frame-audio-mixer](https://github.com/marcus-universe/frame-audio-mixer) | Mixes the microphone for PC streaming and standalone apps |  | MIT | 5 | 2026-11-14 |  |
| [groffta/whisper-frame](https://github.com/groffta/whisper-frame) | Push-to-talk Whisper dictation |  | MIT | 4 | 2026-10-07 |  |

### Desktop and windows (5)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [wayvr-org/wayvr](https://github.com/wayvr-org/wayvr) | Wayland and X11 windows in VR | headset | GPL-3.0 | 1508 | 2026-11-26 |  |
| [Frametop/frametop](https://github.com/Frametop/frametop) | Multi-screen KDE Plasma desktop, 3D mouse and gaze input; ships ft-camd (tracking-camera frames into a shared-memory ring) and camera hand… | headset | MIT | 428 | 2026-11-26 |  |
| [AstronautCheetah/frame-tweaks](https://github.com/AstronautCheetah/frame-tweaks) | Tweak installer | headset | MIT | 5 | 2026-11-26 | yes |
| [SteamFramelyHomebrew/framely](https://github.com/SteamFramelyHomebrew/framely) | Spatial launcher |  | AGPL-3.0 | 5 | 2026-10-30 |  |
| [tovakai/frametop](https://github.com/tovakai/frametop) | Frametop fork with a plugin framework |  | MIT | 5 | 2026-11-01 |  |

### Overlays and HUDs (10)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [wayvr-org/wayvr](https://github.com/wayvr-org/wayvr) | Wayland and X11 windows in VR | headset | GPL-3.0 | 1508 | 2026-11-26 |  |
| [sasaken1102r/frame-mic-tuner](https://github.com/sasaken1102r/frame-mic-tuner) | Microphone echo and noise settings panel |  | MIT | 63 | 2026-11-22 |  |
| [sasaken1102r/frame-perf-overlay](https://github.com/sasaken1102r/frame-perf-overlay) | Frame rate, CPU and GPU load, temperatures, power and link overlay | headset | MIT | 55 | 2026-11-26 |  |
| [Toastconcern/FrameStudio](https://github.com/Toastconcern/FrameStudio) | Custom environments |  | AGPL-3.0 | 27 | 2026-11-25 |  |
| [goodpuppies/petplay](https://github.com/goodpuppies/petplay) | Modular overlay and augmented-reality system |  | none found | 24 | 2026-11-26 |  |
| [beko-kerbecotton/framecolor](https://github.com/beko-kerbecotton/framecolor) | Display colour adjustment |  | MIT | 20 | 2026-09-29 |  |
| [AstronautCheetah/frame-tweaks](https://github.com/AstronautCheetah/frame-tweaks) | Tweak installer | headset | MIT | 5 | 2026-11-26 | yes |
| [dhies23/steam-frame-fan-panel](https://github.com/dhies23/steam-frame-fan-panel) | Fan panel in the quick settings: temperature, RPM, manual or automatic |  | GPL-3.0 | 0 | 2026-10-10 |  |
| [PhoenixSheppy/lhctl](https://github.com/PhoenixSheppy/lhctl) | Control your SteamVR Base Stations 2.0 directly from your Steam Frame over Bluetooth | headset | MIT | 0 | 2026-11-26 | yes |
| [sirrenderstudios/Lainframe](https://github.com/sirrenderstudios/Lainframe) | A character companion in the Steam menu |  | other (see repo) | 0 | 2026-10-31 |  |

### Media (6)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [phit/video2webxr](https://github.com/phit/video2webxr) | 360° and VR180 web video through WebXR (Chromium extension) |  | ISC | 17 | 2026-11-16 |  |
| [Cuteminded/JellyXR](https://github.com/Cuteminded/JellyXR) | Jellyfin movies and shows in VR |  | Apache-2.0 | 14 | 2026-11-22 |  |
| [NoricForge/frame-sbs-toggle](https://github.com/NoricForge/frame-sbs-toggle) | Side-by-side 3D toggle (mirror of a deleted repo, unmaintained) |  | none found | 3 | 2026-10-21 |  |
| [nickgkg/FrameCast](https://github.com/nickgkg/FrameCast) | Casts the headset view to a Chromecast, with sound | headset | MIT | 2 | 2026-11-09 |  |
| [isaac-ranger/sleepframe](https://github.com/isaac-ranger/sleepframe) | Sleep sounds |  | MIT | 1 | 2026-10-05 |  |
| [its-ven/FrameDepth](https://github.com/its-ven/FrameDepth) | Media in SteamVR with 3D depth |  | none found | 1 | 2026-10-11 |  |

### Tooling (27)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [spoopyghosty0/frameport](https://github.com/spoopyghosty0/frameport) | Installs and patches games to run on the headset |  | GPL-3.0 | 287 | 2026-11-09 |  |
| [saphid/frame-control](https://github.com/saphid/frame-control) | Cross-platform headset manager over SSH: view, install, files | pc | MIT | 177 | 2026-11-24 |  |
| [nailuj05/framemate](https://github.com/nailuj05/framemate) | Phone companion app |  | GPL-3.0 | 159 | 2026-10-22 |  |
| [saphid/chromium-webxr-steam-frame](https://github.com/saphid/chromium-webxr-steam-frame) | Chromium build with immersive WebXR |  | BSD-3-Clause | 39 | 2026-11-23 |  |
| [bigbossafman/VR-Mod-Vibecoding-Wizard](https://github.com/bigbossafman/VR-Mod-Vibecoding-Wizard) | Claude skill that turns a flat PC game into a VR mod |  | MIT | 32 | 2026-09-06 |  |
| [lhns/steam-frame-nix](https://github.com/lhns/steam-frame-nix) | Nix Home Manager modules for the headset | headset | Apache-2.0 | 25 | 2026-10-17 |  |
| [travelerdev/frameloader](https://github.com/travelerdev/frameloader) | Sideloads APKs and Linux apps |  | MIT | 19 | 2026-11-09 |  |
| [thunderheronight/splat-workshop](https://github.com/thunderheronight/splat-workshop) | Turns colour-camera recordings into Gaussian splats |  | GPL-3.0 | 14 | 2026-10-28 |  |
| [chaosfox26/framey](https://github.com/chaosfox26/framey) | Plugin loader | headset | GPL-2.0 | 12 | 2026-11-25 |  |
| [Cogential/frametanium](https://github.com/Cogential/frametanium) | App installer and updater that discovers Frame projects |  | none found | 12 | 2026-10-22 |  |
| [frame-commons/charge-watch](https://github.com/frame-commons/charge-watch) | Loud warnings (and optional phone push and auto-shutdown) when a Steam Frame is plugged in but not charging | headset | MIT | 9 | 2026-11-20 | yes |
| [chaosfox26/framey-app](https://github.com/chaosfox26/framey-app) | Installer for Framey |  | GPL-2.0 | 6 | 2026-10-26 |  |
| [curiousjtuber/curiousj-framekit](https://github.com/curiousjtuber/curiousj-framekit) | Setup scripts: Tailscale, distrobox from Desktop Mode, mouse cursor | headset | other (see repo) | 6 | 2026-11-26 |  |
| [miyu0-bit/frameeye-helper](https://github.com/miyu0-bit/frameeye-helper) | Installer for frameeyeosc |  | MIT | 6 | 2026-09-30 |  |
| [AstronautCheetah/frame-tweaks](https://github.com/AstronautCheetah/frame-tweaks) | Tweak installer | headset | MIT | 5 | 2026-11-26 | yes |
| [frame-commons/catalog](https://github.com/frame-commons/catalog) | Catalog of Steam Frame community software, the steam-frame.yml manifest spec, and a compatibility table | pc | other (see repo) | 3 | 2026-11-27 | yes |
| [chaosfox26/frame-fan](https://github.com/chaosfox26/frame-fan) | Fan control |  | GPL-2.0 | 2 | 2026-10-26 |  |
| [DevctioN/FrameConnect](https://github.com/DevctioN/FrameConnect) | Monitoring and file transfer |  | MIT | 2 | 2026-10-25 |  |
| [Inazumanotenshi/Framey-Plugins](https://github.com/Inazumanotenshi/Framey-Plugins) | Plugins for the Framey loader |  | none found | 2 | 2026-11-13 |  |
| [Crypto90/frameload](https://github.com/Crypto90/frameload) | Installs and ports Android VR games to the Frame |  | GPL-3.0 | 1 | 2026-10-29 |  |
| [HynoR/frameclash](https://github.com/HynoR/frameclash) | Clash Meta proxy and panel |  | other (see repo) | 1 | 2026-11-09 |  |
| [SteffanDonal/steam-frame-stuff](https://github.com/SteffanDonal/steam-frame-stuff) | Assorted scripts and notes |  | none found | 1 | 2026-10-16 |  |
| [superpaiku/plusmenu-settings](https://github.com/superpaiku/plusmenu-settings) | Show or hide apps in the dashboard's + menu |  | MIT | 1 | 2026-10-26 |  |
| [dhies23/steam-frame-fan-panel](https://github.com/dhies23/steam-frame-fan-panel) | Fan panel in the quick settings: temperature, RPM, manual or automatic |  | GPL-3.0 | 0 | 2026-10-10 |  |
| [frame-commons/xr-tweak](https://github.com/frame-commons/xr-tweak) | Per-app render resolution, sharpening and foveation level for OpenXR apps on the Steam Frame (an implicit OpenXR layer) | headset | other (see repo) | 0 | 2026-11-18 | yes |
| [JonahSimon/steam-frame-harness](https://github.com/JonahSimon/steam-frame-harness) | Drives the headset with nobody wearing it, for testing |  | MIT | 0 | 2026-11-18 |  |
| [nihas101/steamos-scripts](https://github.com/nihas101/steamos-scripts) (archived) | Install scripts for tools on SteamOS |  | MIT | 0 | 2025-12-06 |  |

### Compatibility fixes (10)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [spoopyghosty0/frameport](https://github.com/spoopyghosty0/frameport) | Installs and patches games to run on the headset |  | GPL-3.0 | 287 | 2026-11-09 |  |
| [saphid/chromium-webxr-steam-frame](https://github.com/saphid/chromium-webxr-steam-frame) | Chromium build with immersive WebXR |  | BSD-3-Clause | 39 | 2026-11-23 |  |
| [Rangermike96/steam-frame-audio-fix](https://github.com/Rangermike96/steam-frame-audio-fix) | USB and Bluetooth audio fix |  | MIT | 7 | 2026-10-16 |  |
| [jareqpl/steam-frame-fixes](https://github.com/jareqpl/steam-frame-fixes) | Proton and Turnip fixes for games |  | MIT | 6 | 2026-10-07 |  |
| [AstronautCheetah/frame-tweaks](https://github.com/AstronautCheetah/frame-tweaks) | Tweak installer | headset | MIT | 5 | 2026-11-26 | yes |
| [daniel-lynch/ovrplugin-openxr-shim](https://github.com/daniel-lynch/ovrplugin-openxr-shim) | OVRPlugin ABI on top of OpenXR |  | MIT | 5 | 2026-09-23 |  |
| [Molier/openxr-dispatcher-open](https://github.com/Molier/openxr-dispatcher-open) | Open dispatcher for converted Quest APKs |  | other (see repo) | 5 | 2026-10-06 |  |
| [Crypto90/frameload](https://github.com/Crypto90/frameload) | Installs and ports Android VR games to the Frame |  | GPL-3.0 | 1 | 2026-10-29 |  |
| [Puffy288/steamvr-home-frame](https://github.com/Puffy288/steamvr-home-frame) | Experimental SteamVR Home installer |  | other (see repo) | 1 | 2026-10-25 |  |
| [AnotherMike-exe/SteamFrameDongleFix](https://github.com/AnotherMike-exe/SteamFrameDongleFix) | Fixes stutter with the rtw89 wireless dongle | pc | MIT | 0 | 2026-11-03 |  |

### Games and ports (27)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [SpeedBreakerProject/speedbreaker](https://github.com/SpeedBreakerProject/speedbreaker) | Unofficial static recompilation of the Xbox 360 version of Need for Speed: Most Wanted (2005): a native port for Steam Deck, Steam Machine,… |  | GPL-3.0 | 728 | 2026-11-25 |  |
| [SpeedBreakerProject/speedbreaker-carbon](https://github.com/SpeedBreakerProject/speedbreaker-carbon) | Unofficial static recompilation of the Xbox 360 version of Need for Speed: Carbon (2006): a native port for Steam Deck, Steam Machine, Stea… |  | GPL-3.0 | 76 | 2026-11-09 |  |
| [bigbossafman/VR-Mod-Vibecoding-Wizard](https://github.com/bigbossafman/VR-Mod-Vibecoding-Wizard) | Claude skill that turns a flat PC game into a VR mod |  | MIT | 32 | 2026-09-06 |  |
| [Cesarus85/mjolnir-vr](https://github.com/Cesarus85/mjolnir-vr) | Ringfall: Mjolnir VR – an unofficial VR mod for Halo: Combat Evolved on Meta Quest 3/3S and Steam Frame. Bring your own disc image. |  | AGPL-3.0 | 25 | 2026-11-19 |  |
| [dividebysandwich/stealth-mission-89](https://github.com/dividebysandwich/stealth-mission-89) | A spiritual successor to old DOS stealth fighter simulations, with dynamic realtime campaign, multiplayer and VR support |  | GPL-3.0 | 14 | 2026-11-26 |  |
| [ClassicWasTaken/HaloSteamFrameMod](https://github.com/ClassicWasTaken/HaloSteamFrameMod) | Community Halo CE VR mod installer for Steam Frame. No retail game executable, ISO, maps, keys, or soundtrack included. Supply your own aut… |  | other (see repo) | 9 | 2026-10-07 |  |
| [PodeCaradox/GalaxyFrame](https://github.com/PodeCaradox/GalaxyFrame) | GalaxyFrame: Mario in VR on Steam Frame, a native port built on the Petari decompilation. Bring your own game files. 100% made by AI (Claud… |  | Unlicense | 9 | 2026-10-07 |  |
| [astromaddie/oot-vr](https://github.com/astromaddie/oot-vr) | Ocarina of Time VR port |  | none found | 6 | 2026-10-20 |  |
| [astromaddie/goldeneye-vr](https://github.com/astromaddie/goldeneye-vr) | GoldenEye 007 VR (MrSco/goldeneye-vr) retargeted to the Valve Steam Frame |  | MIT | 4 | 2026-10-11 |  |
| [astromaddie/time-crisis-vr](https://github.com/astromaddie/time-crisis-vr) | Time Crisis VR port |  | MIT | 4 | 2026-10-11 |  |
| [astromaddie/gen1recomp-frame](https://github.com/astromaddie/gen1recomp-frame) | Native ARM64 Linux OpenXR port kit for Gen1Recomp on Steam Frame; player-supplied game data and separately fetched voxel mod. |  | MIT | 3 | 2026-10-12 |  |
| [astromaddie/gta3-vr](https://github.com/astromaddie/gta3-vr) | GTA III VR port |  | none found | 3 | 2026-10-11 |  |
| [astromaddie/lambda1-vr](https://github.com/astromaddie/lambda1-vr) | Lambda1VR (Half-Life VR) retargeted to the Valve Steam Frame |  | GPL-3.0 | 3 | 2026-10-11 |  |
| [astromaddie/fzerox-vr](https://github.com/astromaddie/fzerox-vr) | Experimental standalone F-Zero X VR for Steam Frame, based on G-Diffuser. Bring your own game data. |  | other (see repo) | 2 | 2026-10-11 |  |
| [astromaddie/gtasa-vr](https://github.com/astromaddie/gtasa-vr) | GTA San Andreas VR port |  | other (see repo) | 2 | 2026-10-11 |  |
| [astromaddie/mariokart64-vr](https://github.com/astromaddie/mariokart64-vr) | Mario Kart 64 VR port |  | GPL-3.0 | 2 | 2026-10-11 |  |
| [astromaddie/vicecity-vr](https://github.com/astromaddie/vicecity-vr) | Experimental standalone Vice City VR for Steam Frame. Tracked weapons and driving, 3D cinema, first/third-person views and live camera sett… |  | other (see repo) | 2 | 2026-10-11 |  |
| [astromaddie/banjo-vr](https://github.com/astromaddie/banjo-vr) | Banjo-Kazooie VR for the Steam Frame (BanjoRecomp + RT64 + OpenXR) |  | GPL-3.0 | 1 | 2026-10-13 |  |
| [astromaddie/dk64-vr](https://github.com/astromaddie/dk64-vr) | Donkey Kong 64 VR for the Steam Frame (DK64 Recompiled + RT64 + OpenXR) |  | GPL-3.0 | 1 | 2026-10-13 |  |
| [astromaddie/fzerox-frame-source](https://github.com/astromaddie/fzerox-frame-source) | Source dependency of the F-Zero X port |  | CC0-1.0 | 1 | 2026-11-10 |  |
| [astromaddie/libultraship-fzerox-frame](https://github.com/astromaddie/libultraship-fzerox-frame) | Source dependency of the F-Zero X port |  | MIT | 1 | 2026-11-10 |  |
| [astromaddie/wipeout-vr](https://github.com/astromaddie/wipeout-vr) | WipEout Steam Frame standalone VR port (fork of phoboslab/wipeout-rewrite) |  | none found | 1 | 2026-10-11 |  |
| [aussie1579/hw2-frame-vr](https://github.com/aussie1579/hw2-frame-vr) | Proof-of-concept VR mod for Homeworld 2 Remastered on the Steam Frame: opengl32.dll proxy with synchronized stereo, a head-tracked game cam… |  | MIT | 1 | 2026-10-20 |  |
| [ElHombreAlex/FTL-Faster-Than-Light-VR](https://github.com/ElHombreAlex/FTL-Faster-Than-Light-VR) | Unofficial VR mod for FTL: Faster Than Light. Requires an owned copy of FTL. Follow the setup before launching, it won't work otherwise. |  | MIT | 1 | 2026-10-05 |  |
| [astromaddie/sfvr](https://github.com/astromaddie/sfvr) | Shared helpers behind a set of VR ports |  | MIT | 0 | 2026-10-11 |  |
| [astromaddie/sm64-vr](https://github.com/astromaddie/sm64-vr) | Super Mario 64 (sm64coopdx) native standalone VR port for Valve Steam Frame |  | none found | 0 | 2026-10-13 |  |
| [josethevrtech/magicshelf-sonic-tiger](https://github.com/josethevrtech/magicshelf-sonic-tiger) | Sonic Tiger LCD handheld for MagicShelf on Steam Frame. Internet Archive player, no ROM import. |  | GPL-3.0 | 0 | 2026-10-27 |  |

### Hardware (3)

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [Nieko27/Frame-Workshop](https://github.com/Nieko27/Frame-Workshop) | Open hardware designs |  | CERN-OHL-S-2.0 | 107 | 2026-11-20 |  |
| [DeeJanuz/steam-frame-pd100-mount](https://github.com/DeeJanuz/steam-frame-pd100-mount) | Mount |  | MIT | 17 | 2026-10-09 |  |
| [ravngr/3dscan-ArcturusCamera](https://github.com/ravngr/3dscan-ArcturusCamera) | 3D scan of the colour camera module |  | CC-BY-SA-4.0 | 0 | 2026-10-13 |  |

### Not sorted yet (34)

Tagged `steam-frame` on GitHub, with no manifest and no curated entry yet.

| Project | What it does | Runs on | Licence | Stars | Last push | Manifest |
|---|---|---|---|---|---|---|
| [TaiKeid/steam-frame-full-keyboard](https://github.com/TaiKeid/steam-frame-full-keyboard) | Steam Frame keyboard: full-size replacement for the built-in VR keyboard. Ctrl, Alt, F-keys, swipe typing, dictation, and 47 languages. |  | MIT | 114 | 2026-11-21 |  |
| [FauxxYT/StreamXR](https://github.com/FauxxYT/StreamXR) | Watch YouTube in VR on the Steam Frame and SteamVR headsets! |  | other (see repo) | 36 | 2026-11-10 |  |
| [seaweeduk/VideoFrameVR](https://github.com/seaweeduk/VideoFrameVR) | VR video player for the Steam Frame and Linux SteamVR: smooth 8K HEVC playback, eye-tracked foveated rendering at 120 Hz, passthrough video… |  | GPL-3.0 | 31 | 2026-11-23 |  |
| [guix8/framedepth](https://github.com/guix8/framedepth) | Real-time 2D-to-3D for video and images in Chrome on the Steam Frame (unofficial) |  | GPL-3.0 | 20 | 2026-11-14 |  |
| [RxVreality/UTMTFTM](https://github.com/RxVreality/UTMTFTM) | Easy offset for SteamVR hands: grab your in-game hand and put it where it belongs, live. |  | MIT | 14 | 2026-11-25 |  |
| [Wurby/sideframe](https://github.com/Wurby/sideframe) | Your Mac desktop in your Steam Frame, as a SteamVR dashboard tab |  | MIT | 7 | 2026-11-17 |  |
| [HynoR/frame-vrc](https://github.com/HynoR/frame-vrc) | Running PC Version VRchat On Steam Frame |  | Apache-2.0 | 6 | 2026-11-09 |  |
| [ObeseCatLord/Gurumin-Enhanced-Rendering](https://github.com/ObeseCatLord/Gurumin-Enhanced-Rendering) | High-resolution ultrawide rendering, smooth frame interpolation, free camera and 6DoF VR for Gurumin on Steam — Windows, Linux and standalo… |  | other (see repo) | 6 | 2026-11-23 |  |
| [mog422/index-frame-relay](https://github.com/mog422/index-frame-relay) | Relay Valve Index controllers to Steam Frame's native SteamVR environment, enabling full headset UI interaction and guardian. |  | MIT | 4 | 2026-11-05 |  |
| [Malorn44/steam-frame-polykey](https://github.com/Malorn44/steam-frame-polykey) | On-screen keyboard for Valve Steam Frame: layouts, multi-language input, prediction, swipe-typing, and offline dictation |  | MIT | 2 | 2026-11-26 |  |
| [TakeyaSaito/frame-remote](https://github.com/TakeyaSaito/frame-remote) | SteamVR dashboard buttons on the Steam Frame that run commands on your Linux gaming PC: start/close SteamVR and games, Wake-on-LAN, and any… |  | MIT | 2 | 2026-11-18 |  |
| [cryptofyre/Environmental](https://github.com/cryptofyre/Environmental) | A tool to make your Steam Frame finally something worth living in. |  | none found | 1 | 2026-11-23 |  |
| [EncidXVII/WristXR](https://github.com/EncidXVII/WristXR) | VR desktop overlay for SteamVR: your screens in VR, a VR keyboard and a wrist watch. Windows and Linux. |  | GPL-3.0 | 1 | 2026-11-25 |  |
| [GREYBE4RD/vrperf](https://github.com/GREYBE4RD/vrperf) | A lightweight, native Linux performance overlay for SteamVR, written in Rust. It displays PCVR frame timings and system statistics inside t… |  | GPL-3.0 | 1 | 2026-11-23 |  |
| [RxVreality/Portaballs](https://github.com/RxVreality/Portaballs) | VR proof of concept: throw paint by hand and the splats become portals you can walk through. Runs on s&amp;box built from source. |  | other (see repo) | 1 | 2026-11-21 |  |
| [sframelab/frame-hands](https://github.com/sframelab/frame-hands) | Experimental hand tracking for Steam Frame, with SteamVR input and a dashboard toggle. |  | MIT | 1 | 2026-10-15 |  |
| [steamlua/SteamLuaTools](https://github.com/steamlua/SteamLuaTools) | Steam LuaTools Plugin extends Millennium on desktop and Steam Deck, indexing luatools, opensteamtool, and slssteam utilities. Manage manife… |  | MIT | 1 | 2026-11-21 |  |
| [adepssimius/frame-lights-out](https://github.com/adepssimius/frame-lights-out) | Framey plugin: turn off the Steam Frame's status LED from SteamVR Quick Settings |  | MIT | 0 | 2026-11-16 |  |
| [C0ldbloodthe0ry/korg-gadget-vr-steamvr](https://github.com/C0ldbloodthe0ry/korg-gadget-vr-steamvr) | Unofficial fix for KORG Gadget VR on SteamVR: controller bindings and a view-height mod. Free to use, no credit needed. |  | MIT-0 | 0 | 2026-11-23 |  |
| [dividebysandwich/neon-lasertag](https://github.com/dividebysandwich/neon-lasertag) | A fun and fast laser tag experience in 2D and VR |  | none found | 0 | 2026-11-12 |  |
| [Echazu/time-crisis-vr](https://github.com/Echazu/time-crisis-vr) | Play Time Crisis in VR on Meta Quest and PCVR with tracked pistol aiming, stereo rendering, original arcade gameplay, and physical ducking… |  | none found | 0 | 2026-11-06 |  |
| [Elter71/magic-keyboard-linux-pair](https://github.com/Elter71/magic-keyboard-linux-pair) | Pair an Apple Magic Keyboard over the USB cable on Linux / Steam Frame, like macOS does |  | GPL-3.0 | 0 | 2026-11-20 |  |
| [EncidXVII/FoveaXR](https://github.com/EncidXVII/FoveaXR) | Foveated rendering for SteamVR and OpenXR games: less GPU work per frame on any PC VR headset. |  | GPL-3.0 | 0 | 2026-11-25 |  |
| [EncidXVII/SweatXR](https://github.com/EncidXVII/SweatXR) | VR fitness tracker for every SteamVR game: calories, active minutes and heart rate. Your data stays on your PC. |  | GPL-3.0 | 0 | 2026-11-25 |  |
| [Futuremappermydud/hexecutor-frame](https://github.com/Futuremappermydud/hexecutor-frame) | Open Source Steam Frame cDSP/Hexagon Runtime |  | none found | 0 | 2026-11-23 |  |
| [GlitchNullCore/Thirl](https://github.com/GlitchNullCore/Thirl) | Free PC VR and desktop streaming from Windows to Quest, PICO, Steam Frame and other supported headsets. |  | none found | 0 | 2026-11-18 |  |
| [Haritan4141/SteamFrame-QuestStyle-VRChat-Bindings](https://github.com/Haritan4141/SteamFrame-QuestStyle-VRChat-Bindings) | Quest-style controller bindings for Steam Frame in VRChat. Fixes unreliable finger gestures while preserving standard controls. |  | none found | 0 | 2026-11-21 |  |
| [information-redacted/framedragfix](https://github.com/information-redacted/framedragfix) | a fix for OVRAS SpaceDrag remote panel misalignment when streaming with the Steam Frame |  | none found | 0 | 2026-11-16 |  |
| [lostpanda85/frame-docs](https://github.com/lostpanda85/frame-docs) | Unofficial developer notes for the Steam Frame's OS: services, APIs, hardware, kernel, boot and firmware, all verified on-device |  | MIT | 0 | 2026-11-21 |  |
| [Mass1milian0/FrameSync](https://github.com/Mass1milian0/FrameSync) | Sync your frame clipboard with windows and the other way around - WARNING: VIBECODED |  | none found | 0 | 2026-11-16 |  |
| [TobseF/CozyMarbles-VR-Mod](https://github.com/TobseF/CozyMarbles-VR-Mod) | Stream Frame VR support for the CozyMarbles game |  | MIT | 0 | 2026-11-16 |  |
| [turboncelucionce/steam-frame-drawing-tablet](https://github.com/turboncelucionce/steam-frame-drawing-tablet) | Pen tablet driver for Steam Frame's native desktop |  | GPL-2.0 | 0 | 2026-11-08 |  |
| [TylerK26/framewall](https://github.com/TylerK26/framewall) | An app to stream your main monitor, plus multiple virtual monitors to the steam frame with sunshine and moonlight |  | GPL-3.0 | 0 | 2026-11-25 |  |
| [vaclavik-xyz/stream-frame](https://github.com/vaclavik-xyz/stream-frame) | Live picture and sound from a VR headset compositor to any screen: Vulkan implicit layer -&gt; shm ring -&gt; ffmpeg -&gt; HLS + RTSP/WebRTC |  | MIT | 0 | 2026-11-01 |  |

147 projects, 6 with a `steam-frame.yml`.
<!-- catalog:end -->

## How it's built

`fc-catalog build` reads the curated list, searches GitHub for the `steam-frame` topic and
fetches each repo's `steam-frame.yml`. It then writes `catalog.json`, the tables above,
[COMPAT.md](COMPAT.md) and [PROBLEMS.md](PROBLEMS.md) (manifests that failed to parse).
A weekly GitHub Action runs it. It reads only public data and sends nothing anywhere.

```sh
pip install pyyaml
bin/fc-catalog check path/to/steam-frame.yml   # check a manifest
bin/fc-catalog build                           # rebuild everything (uses GITHUB_TOKEN or `gh auth token` if present)
python3 -m unittest discover tests             # tests, no network
```

Part of [frame-commons](https://github.com/frame-commons). Not affiliated with Valve. Made with help from Claude.

**Licences:** the code is MIT ([LICENSE](LICENSE)). The manifest spec is CC0 ([spec/LICENSE](spec/LICENSE)).
The catalog data (`catalog.json`, the tables, COMPAT.md) is CC0 too: copy it into anything.
