# Steam Frame field guide

Which open tools to reach for, area by area, for the Valve Steam Frame (SteamOS on ARM64). The
[catalog](README.md) lists everything we have found. This guide picks from it, says why, and says what
the evidence is.

**Last reviewed 2026-11-01.** Stars, licences and push dates are as of that day. Frame software moves
weekly, so treat anything older than a month as possibly stale.

**How this was put together.** From each project's README, its GitHub metadata, its issue tracker and
Valve's public documentation. It is not a hands-on test of every tool. "Per its README" means the
claim is the project's own and we have not reproduced it. Where nobody has published evidence, we say
so.

**Corrections are welcome.** If a pick is wrong, out of date or unfair, open a pull request against
this file or an issue. Maintainers of listed projects: a `tested:` record in your
[`steam-frame.yml`](spec/steam-frame-yml.md) is the best evidence you can give, and it lands in
[COMPAT.md](COMPAT.md).

## Selection criteria

A tool is a pick when it meets most of these, and the text says which ones it misses:

1. **Source is public.** Open source is preferred. Source-available or unlicensed code is flagged
   ("no licence file" means the code is public but not open source until its author adds one).
   Closed tools appear only where they are the only option, or where Valve's own built-in feature is
   the right answer (listed first and marked closed).
2. **Maintained.** A push in the last few weeks, issues answered.
3. **Evidence it works on the Frame.** A README that names the headset OS or SteamVR version it was
   tested on, a test record, or an issue thread from users.
4. **Licence clarity,** including for model weights and bundled third-party parts.
5. **No telemetry.** We don't recommend tools that send usage data. Where a dependency does, it is
   noted.

Valve's own features count as options too, and where one is the right answer it is listed first.

**Disclosure.** This guide is written by frame-commons' admin (@arealjim). One listed project belongs
to this org ([frame-commons/catalog](https://github.com/frame-commons/catalog)) and one to the admin
personally ([arealjim/frame-stream](https://github.com/arealjim/frame-stream)). Both are marked
"(maintained by this org's admin)" and are not ranked above alternatives without public evidence.

## Before you install anything

- **Most community tools install into your home folder** with a `curl … | bash` line run in desktop
  mode. Home survives OS updates; the read-only system image does not keep changes. Read the script
  first.
- **Developer Mode** (Settings → System) turns on SSH and other developer access; many tools need it.
  See Valve's
  [Frame setup page](https://partner.steamgames.com/doc/steamhardware/steamframe/setup). Set a strong
  password when you turn it on: with SSH enabled, anyone on your network who knows it can log in.
- **Many projects are weeks old and tested on one headset,** so "works for the author" is often the
  whole evidence.
- **Updates break things.** Where a README names a headset OS version, it is usually 0.3.x or 0.4.x.
  SteamOS 0.5.6 is on the beta channel as of this review (per
  [Frame Control's notes](https://github.com/saphid/frame-control/blob/main/docs/steamos-2026-10-compat.md)),
  and almost nothing has been reported against it yet.
- **Tools that drive Steam's own UI** (pressing buttons, injecting into the Steam client) usually need
  *CEF Remote Debugging* turned on in Steam's developer settings. That is a debugging interface;
  decide whether you want it left on.

---

## Streaming from a PC

**Pick: Valve's own Steam Link VR streaming** from a PC, over Wi-Fi or the bundled wireless adapter.
Windows is the host Valve documents; Linux hosts work for many users (see below). Nothing to
install on the headset, and it does eye-tracked foveated streaming.

- *Evidence:* Valve's supported path.
- *Linux hosts:* launch-month reports varied by distribution, desktop session and GPU. If a VR
  title launched from the headset never starts SteamVR, see
  [SteamVR-for-Linux #962](https://github.com/ValveSoftware/SteamVR-for-Linux/issues/962) for the
  workarounds people used (start SteamVR on the desktop first; one commenter also needed
  `PRESSURE_VESSEL_IMPORT_OPENXR_1_RUNTIMES=1`). Valve closed the issue on 2026-09-27, saying a fix
  was in progress; we found no later note that it has shipped, so the workarounds may still be needed.
- *Limits:* closed source; no macOS host (see below).

**Main open alternative: [WiVRn](https://github.com/WiVRn/WiVRn)** (GPL-3.0, 1831★, pushed
2026-10-30), for Linux hosts that want an open OpenXR stack (Monado-based).

- *Evidence:* a native Frame client was merged on 2026-09-27
  ([PR #1130](https://github.com/WiVRn/WiVRn/pull/1130)); the PR author reports audio, H.264/H.265
  8-bit video and both Touch and Frame controller profiles working. CI builds it in Valve's Steam
  Runtime 4 arm64 SDK image (`wivrn-frame-client.zip`).
- *Choose it when:* you are on Linux, want to stream through Monado, or want to tune the encoder.
- *Limits:* the newest tagged release (v26.9, 2026-09-12) predates Frame support, so you need a CI
  build. Open Frame issues include double vision on lobby hands and lasers
  ([#1140](https://github.com/WiVRn/WiVRn/issues/1140)), jitter on some units
  ([#1173](https://github.com/WiVRn/WiVRn/issues/1173)) and reconnect failures after a refresh-rate
  change ([#1181](https://github.com/WiVRn/WiVRn/issues/1181)). The client must be added to Steam
  and launched from the library, or the OpenXR loader is not found. As of the PR, no 10-bit or AV1
  decode on the headset's kernel. Linux host only.
  [ALVR](https://github.com/alvr-org/ALVR) has no Frame client yet
  ([#3411](https://github.com/alvr-org/ALVR/issues/3411)).

**For flat games and the desktop: [Moonlight XR for Frame](https://github.com/simplysanatori/moonlight-xr-steam-frame)**
(GPL-3.0, 17★, pushed 2026-11-01), a native port of Sean Gilleece's
[Moonlight XR](https://github.com/Gilleece/moonlight-android-xr), a client for [Sunshine](https://github.com/LizardByte/Sunshine)
or [Apollo](https://github.com/ClassicOldSong/Apollo) hosts.

- *Evidence:* v1.1.1 stable; per its README, used on one Frame (SteamOS 0.4.5, SteamVR 2.18)
  against one Windows PC. Hardware H.264/HEVC decode, 72–144 Hz, Wi-Fi, adapter or USB cable.
- *Choose it over Valve's flat streaming when:* you want a curved or 3D screen, per-button
  controller remapping, Apollo's virtual display, or a non-Steam host.
- *Limits:* single-tester evidence. The older
  [Lepton-based build](https://github.com/simplysanatori/moonlight-xr-lepton) is the fallback if
  the native one misbehaves.

**Helpers for PC streaming**

- [SteamFrameDongleFix](https://github.com/AnotherMike-exe/SteamFrameDongleFix) (MIT): for Linux
  hosts whose desktop freezes for seconds at a time while the wireless adapter is plugged in. New
  (2026-10-27), no stars yet; needs kernel 7.2+ with rtw89 debugfs.
- [Frame Control](https://github.com/saphid/frame-control) ships a Linux wireless-adapter doctor
  (see Tooling).
- [Frame Audio Mixer](https://github.com/marcus-universe/frame-audio-mixer) (MIT): mixes headset-app
  audio with the mic and sends it to the PC as the streaming microphone.
- [steam-frame-chroma-key](https://github.com/spyjacob/steam-frame-chroma-key) (MIT): chroma-key
  mixed reality for PC streaming.

## Streaming from a Mac

**There is no Valve option:** SteamVR dropped macOS in 2020, so Steam Link VR streaming needs a
Windows or Linux PC.

**Open options, both young:**

- **[OXRSys](https://github.com/demonixis/oxrsys)** (MPL-2.0, 114★, pushed 2026-11-01) is an
  open-source OpenXR runtime for macOS (Metal, MoltenVK, VideoToolbox H.264/H.265). Upstream ships
  clients for Quest, Pico and Vision Pro. Its Steam Frame client is an open draft,
  [PR #30](https://github.com/demonixis/oxrsys/pull/30), not merged.
- **[frame-stream](https://github.com/arealjim/frame-stream)** (MIT plus upstream licences for
  patches; **maintained by this org's admin**) builds on OXRSys: it patches the Frame client from
  PR #30 (by nburns), adds Mac-side runtime fixes and engine sample projects (Godot, Unity, Unreal),
  and adds a Wine path for some Windows VR games, building on
  [oxrsys-winebridge](https://github.com/anoshmisiosdev/oxrsys-winebridge). *Evidence:* its own README only. It was published on 2026-10-30, has no outside
  reports yet (no stars or issues), and says it was tested on macOS 27 on Apple Silicon only. Its
  latency and game claims have not been reproduced by anyone else.

As far as we found, these are the only public Mac-to-Frame VR paths. Neither has independent test
reports yet. Reports from other Mac users would be the most useful addition to this section.

**For flat content from a Mac:** Moonlight XR (above) against a Sunshine host on macOS, or Steam's
own Remote Play for flat games, should work in principle. *We found no published report of either
from a Mac to a Frame.*

## Desktop and windows in VR

**Valve's built-in desktop** (Launch a program → Desktop) is a single KDE Plasma screen floating in
VR. It is there on every headset and is the baseline.

**Pick for a full desktop: [Frametop](https://github.com/Frametop/frametop)** (MIT, 330★, pushed
2026-10-29). Several KDE screens of any size and shape around you, app windows pulled out into their
own panels, a mouse pointer that works across all of SteamVR, and experimental gaze pointing.

- *Evidence:* per its README, tested on SteamOS 0.4.5; ships a `scripts/doctor.sh` that checks what
  an update moved or deleted. Stable and experimental channels; prebuilt releases. Has a Discord and an
  issue tracker.
- *Limits:* about 3 GB of disk (it installs a distrobox build container in your home folder). It
  pauses during VR games by default, to hand the game the headset (configurable). Gaze mode reads eye-tracker data that SteamOS 0.4 moved once already,
  so it may need an update after headset updates.

**Alternative: [WayVR](https://github.com/wayvr-org/wayvr)** (GPL-3.0, 1470★, pushed 2026-10-30),
the long-standing Linux VR overlay (formerly wlx-overlay-s).

- *Choose it when:* you want individual apps floating around you rather than a full KDE desktop, or
  you already use it on a Linux PC.
- *Limits:* its README calls Frame support experimental. On the Frame it runs headless, without your
  KDE desktop, and the aarch64 AppImage currently comes from nightly CI builds, which need a GitHub
  login to download.

**Also worth knowing**

- [tovakai/frametop](https://github.com/tovakai/frametop) (MIT): a Frametop fork adding a plugin
  framework.
- [Framely](https://github.com/SteamFramelyHomebrew/framely) (AGPL-3.0): a spatial launcher, created 2026-10-03.
- [Frame Tweaks](https://github.com/AstronautCheetah/frame-tweaks) and
  [steam-frame-nix](https://github.com/lhns/steam-frame-nix) fix many desktop-mode rough edges
  (clipboard, keyboard, KDE wallet, window curvature); see Tooling.

## Hands

**Nothing solid yet.** Every camera-based hand tracker for the Frame calls itself experimental.

**Valve's controllers** sense finger positions capacitively (per Valve's product description). If
you only need finger poses in social VR, that is the stable option.

**Experimental projects, for people who want to help:**

- [steam-frame-hand-tracking](https://github.com/spyjacob/steam-frame-hand-tracking) (MIT, pushed
  2026-10-17): bare hands in PC-streamed games, tracked on the headset and sent to the PC as Frame
  controllers. *Limits, per its README:* it runs the headset CPU hot (hottest core in the high 80s °C,
  peaks of 93–95 °C, and the headset rebooted once under heavy load), has a thermal watchdog, is laggy on fast wrist turns, and adds a Vulkan layer
  to the SteamVR compositor.
- Frametop's [hands module](https://github.com/Frametop/frametop/blob/main/hands/README.md) (MIT
  code): IR-camera hand tracking with MediaPipe models on ncnn, used for hand cut-outs and pinch
  clicks. *Limits:* held back from the stable channel ("deferred") because of its CPU cost; the
  experimental channel's installer offers it, on by default. The stock
  MediaPipe models are Apache-2.0; its fine-tuned models on Hugging Face are
  [CC BY-NC 4.0](https://huggingface.co/DeeJanuz/frametop-hands-models), so not for commercial use.
- [frame-hands](https://github.com/eyfeldb/frame-hands) (MIT): headset tracker plus SteamVR driver
  and Windows bridge. *Limits:* trained models and runtime assets are not included, so it can't run
  from the repository alone.

**Elsewhere:** Monado's Mercury tracker (BSL-1.0) is an open optical hand tracker used with other
headsets. We found no Frame port.

## Eyes and face

**Pick for gaze and blinks in social VR: SteamVR's own eye-tracking OSC** over Steam Link. Nothing to
install on the headset: a SteamVR setting plus a VRCFaceTracking module.

**Pick when you want more: [frameeyeosc](https://github.com/sasaken1102r/frameeyeosc)** (sasaken1102r's
fork; MIT, 115★, pushed 2026-11-01). It adds smoothing, per-user eyelid calibration and, with the eye
cameras, widened eyes, squints and pupil size. It outputs OSC, LiveLink or its own VRCFaceTracking
module.

- *Evidence:* detailed README with a side-by-side comparison against SteamVR's own OSC (on SteamVR
  2.18.2), notes on SteamOS 0.4.3 behaviour, sends values only to your PC. Japanese README too.
- *Limits:* eyelid data comes from an internal shared-memory file, not a public API, so a headset
  update can break it. The README already documents behaviour changes in SteamOS 0.4.3.
- The [original frameeyeosc](https://github.com/konsti219/frameeyeosc) (MIT) is the proof of concept
  it forked from; its own README points users to Babble instead.
  [frameeye-helper](https://github.com/miyu0-bit/frameeye-helper) (MIT) is a one-button installer
  for frameeyeosc.

**Pick for expressions and mouth: [Babble Frame Runtime](https://github.com/Project-Babble/Babble-Frame-Runtime)**
(GPL-3.0, 41★, pushed 2026-10-31). Eye openness, widen and pupil dilation from the eye cameras, plus
43 mouth blendshapes from a wired Babble face tracker, sent to VRCFaceTracking. Installs as a SteamVR
driver with a settings page and pauses the cameras when the headset is off your head.

- *Limits:* its README calls the models prototypes and the project a work in progress. Mouth tracking
  needs Babble's tracker hardware. It currently needs a specific VRCFaceTracking module linked from the
  README.

**Alternatives:** [vrcft-steam-frame](https://github.com/hakumaguro/vrcft-steam-frame) (MIT), a
VRCFaceTracking module with a guided tuning tool, tested on Windows 11 per its README.
[FrameEyeCameraFeed](https://github.com/Curtis-VL/FrameEyeCameraFeed) (MIT) serves the eye-camera
feeds to EyeTrackVR, for people who run their own models.

## Passthrough

**Valve's Room View** is built in: double-press the headset's side button or the Steam button on
either controller.

**Pick for hands-free toggling: [KnockThru](https://github.com/VioletTides/KnockThru)** (MIT, 12★,
pushed 2026-10-28). Knock twice on the headset to see the room; three times to switch between
blended and room-only. SquintThru (below) is also hands-free but has no licence file.

- *Evidence:* CI, and its detector is tested against motion recorded on a Frame (the recordings and
  rules are documented).
- *Limits:* needs Developer Mode and CEF Remote Debugging, because it presses Room View in Steam's UI.

**Alternatives**

- [frame-passthrough-shortcuts](https://github.com/KominoVR/frame-passthrough-shortcuts) (MIT):
  thumbstick gestures for blended/opaque passthrough and, with the Arcturus colour module, colour vs
  infrared. No push since 2026-09-25.
- [frame-aux-shortcuts](https://github.com/sasaken1102r/frame-aux-shortcuts) (MIT) puts passthrough,
  among other actions, on the aux button (uses a private SteamVR interface).
- [SquintThru](https://github.com/huntergcook/SquintThru): squint one eye to see the room. *No
  licence file.*
- [frame-autopass](https://github.com/bod09/frame-autopass) (MIT): for the Arcturus colour module,
  switches to infrared passthrough in the dark and back. Tested on SteamOS 0.3.0 / SteamVR 2.17.10
  per its README, so check it on newer versions.
- [frame-passthrough-pip](https://github.com/Sippbox/frame-passthrough-pip) (MIT): the passthrough
  view as a small panel over any game.
- [roommate-radar](https://github.com/danthedaniel/roommate-radar) (AGPL-3.0): highlights people
  nearby with on-headset object detection. Created 2026-10-25.

## Voice and microphone

**Dictation: no single pick yet.** We found five standalone tools, all MIT and all created since late
September. None has independent test reports yet. All run speech recognition on the headset by default. Choose by
how you want to work:

| Tool | Model | Good for | Notes |
|---|---|---|---|
| [FrameYap](https://github.com/baketnk/frame-yap) | Parakeet | Review text before it is typed; SteamVR panel; remappable | Its speech runtime (Moondream/Kestrel) includes upstream telemetry. FrameYap turns it off by default with a patch and refuses to run if the patch can't apply. Large install (about 1–1.5 GB). |
| [steam-frame-dictation](https://github.com/khvn26/steam-frame-dictation) | whisper.cpp `tiny.en`, CPU | Light, always-ready background service | English model by default. |
| [Frame Voice](https://github.com/techieyann/frame-voice) | whisper.cpp `base` or `small` | Controller-triggered, desktop and standalone apps | Per its README, not inside Steam menus or VR games. An optional cloud model (Groq, your own API key) sends audio off the headset; the local models don't. |
| [fuelCell Voice Typing](https://github.com/juanramosjr1/frame-voice) | faster-whisper, CPU | Steam search, browser, Discord; copy/paste chords | Three speed/accuracy settings. |
| [whisper-frame](https://github.com/groffta/whisper-frame) | whisper.cpp `small`, GPU (Vulkan) | Bigger model on the GPU | Push-to-talk; no push since 2026-10-07. |

Frametop and Frame Tweaks also bundle dictation as an option.

**Microphone: [Frame Mic Tuner](https://github.com/sasaken1102r/frame-mic-tuner)** (MIT, 43★,
pushed 2026-10-31). A SteamVR panel that switches echo cancellation and noise suppression per audio
output (speakers, USB-C, Bluetooth) and shows the live signal path. No telemetry, per its README. With
update checks on, it contacts GitHub daily and the author's site for an app list; both can be turned
off.

**Known bug workaround: [steam-frame-audio-fix](https://github.com/Rangermike96/steam-frame-audio-fix)**
(MIT). Brings back external-headphone audio that goes silent when an app opens the mic, a bug still
open at Valve as [SteamOS #2896](https://github.com/ValveSoftware/SteamOS/issues/2896). Tested on one
headset; it warns when your PipeWire version differs from the one it was tested on.

## Input and remapping

**Lighthouse trackers and controllers: [QuestLHSync](https://github.com/CreoleVR/QuestLHSync)** (MIT,
215★, pushed 2026-10-18). Keeps a Lighthouse play space aligned with the Frame's own tracking by
watching base-station flashes with the headset cameras, with nothing mounted on the headset.

- *Evidence:* Frame support by @NotZoeyDev; installs without root on the Frame per its README.

**Headset buttons: [frame-aux-shortcuts](https://github.com/sasaken1102r/frame-aux-shortcuts)** (MIT):
actions for one to five presses, a long press and taps on the headset.

**Mouse and keyboard**

- Frametop's room-anchored mouse pointer (see Desktop) works across the dashboard, Steam and
  overlays, and hands back to the laser when you pick up a controller.
- [frame-unboundedMouse-vibed](https://github.com/Andalu30/frame-unboundedMouse-vibed) (MIT): a mouse
  drives the laser pointer everywhere. *Limits, per its README:* experimental, runs inside SteamVR's
  server, so a bug can blank the headset until you remove it.
- [frame-jp-keyboard](https://github.com/sasaken1102r/frame-jp-keyboard) (MIT): Japanese flick input
  and kana-kanji conversion on the VR keyboard (injects into the Steam client).
- [Frame Input](https://github.com/uxandy/frame-input) (MIT): shares a keyboard and mouse plugged into
  the headset with a streamed Windows PC. *Depends on VirtualHere, which is proprietary.*

**Research and niche:** [FramePicoTracker](https://github.com/Rulez777/FramePicoTracker) (GPL-3.0,
research notes on PICO body trackers), [nso-frame-bridge](https://github.com/MichaelScottsman/nso-frame-bridge)
(Apache-2.0, Switch Online GameCube controller).

## Overlays and HUDs

**Pick: [frame-perf-overlay](https://github.com/sasaken1102r/frame-perf-overlay)** (MIT, 44★, pushed
2026-10-31). Frame rate, CPU and GPU load, temperatures, power, battery and the Steam Link link,
following your head or worn on a controller like a watch.

- *Evidence:* detailed README that is explicit about what each number does and doesn't measure; no
  telemetry beyond an update check.

**Alternatives**

- [FrameColor](https://github.com/beko-kerbecotton/framecolor) (MIT): display colour, gamma and
  presets from the dashboard, via a Vulkan layer in the compositor. No push since 2026-09-29.
- [Frame Studio / Frame Home](https://github.com/Toastconcern/FrameStudio) (AGPL-3.0, pushed
  2026-11-01): custom environments behind the Steam menu and loading screens, with an editor on
  PC/Mac/Linux.
- Fan control: [Fan Control for Framey](https://github.com/chaosfox26/frame-fan) (GPL-2.0) and
  [steam-frame-fan-panel](https://github.com/dhies23/steam-frame-fan-panel) (GPL-3.0). Both need
  root to install, and Fan Control says its cooling components run as root. Changing cooling
  behaviour on a headset you wear is your call; neither has independent reports yet.
- [petplay](https://github.com/goodpuppies/petplay) : a modular overlay system for SteamVR. It has *no licence file*.

## Media

**Nothing solid yet** for local video on the headset. What exists:

- **PC-hosted video and games in 3D:** Moonlight XR (see PC streaming) shows side-by-side and
  top-bottom 3D from the PC, and can turn 2D into 3D with a depth model.
- **Web 360° and VR180 video:** [video2webxr](https://github.com/phit/video2webxr) (ISC), a Chromium
  extension. Its README says it works on the Frame in Chrome Canary set up per
  [a fork](https://github.com/phit/chromium-webxr-steam-frame) of the WebXR Chromium build. No DRM
  video.
- **Jellyfin:** [JellyXR](https://github.com/Cuteminded/JellyXR) (Apache-2.0) works through SteamVR on
  PCs, but its own status table lists the Frame as "waiting for device", so standalone use is
  untested.
- **Casting the headset view to a TV:** [FrameCast](https://github.com/nickgkg/FrameCast) (MIT) casts
  to a Chromecast using the headset's hardware encoder. Tested on one setup.
- **Phone mirroring:** [scrcpy4Frame](https://github.com/xhuytox/scrcpy4Frame) (MIT), a scrcpy wrapper.

## Getting games and apps to run

**Valve first.** [Steam Frame Verified](https://partner.steamgames.com/doc/steamhardware/steamframe/compat)
ratings cover Steam games in standalone mode. Android apps run in Lepton, Valve's Android runtime, and
Valve's Devkit Client can install your own builds.

**Pick for Quest games and sideloading: [FramePort](https://github.com/spoopyghosty0/frameport)**
(GPL-3.0, 228★, pushed 2026-10-26). Converts and patches Quest games for the Frame (through
[OVRPort](https://github.com/Android-XR-Bridge/OVRPort) and Lepton), installs Android, Linux and
Windows apps, and adds them to your Steam library. Runs on Windows, macOS and Linux.

- *Evidence:* the most-starred tool in this area, with an active issue tracker; keeps a
  [list of tested games](https://github.com/spoopyghosty0/frameport/blob/main/docs/GAMES.md) with
  per-game recipes.
- *Limits:* Quest conversion can't fix games that check their licence through the Oculus app; PC VR
  on the headset through Proton is marked experimental; x86-64 Linux apps run through FEX, slower.
  [openxr-dispatcher-open](https://github.com/Molier/openxr-dispatcher-open) describes OVRPort's
  bundled OpenXR dispatcher as closed and offers an open replacement (MIT).

**Alternatives**

- [Frameloader](https://github.com/travelerdev/frameloader) (MIT): drag-and-drop install of APKs,
  Windows apps and Linux ARM64 builds through Valve's devkit protocol. No telemetry, per its README.
- [FrameLoad](https://github.com/Crypto90/frameload) (GPL-3.0): installs and ports Android VR games
  from inside the headset, no PC; uses FramePort for porting.
- FrameDrop, whose install buttons appear in several READMEs, is a free (donationware) sideloader.
  We found no published source (no public repository; its site links none), so it falls outside
  this guide's criteria. Those projects also
  offer plain downloads.

**Specific fixes**

- [Chromium with WebXR](https://github.com/saphid/chromium-webxr-steam-frame) (BSD-3-Clause): a
  Chromium build whose WebXR "Enter VR" works on the Frame. Tested on SteamOS 0.3.0 per its README.
- [steam-frame-fixes](https://github.com/jareqpl/steam-frame-fixes) (MIT): patched Proton and Turnip
  for the native ARM64 World of Warcraft client.
- [ovrplugin-openxr-shim](https://github.com/daniel-lynch/ovrplugin-openxr-shim) (MIT): Meta's
  OVRPlugin API on OpenXR for VrApi-era Quest titles. Its README reports results on a Quest 2, not
  yet on the Frame.
- [steamvr-home-frame](https://github.com/Puffy288/steamvr-home-frame) (MIT for its own code;
  downloaded Valve components keep their own terms): SteamVR Home on the headset, "a fun experiment"
  per its README.
- The audio and wireless-adapter fixes are under Voice and PC streaming.

## Tooling

**Headset manager: [Frame Control](https://github.com/saphid/frame-control)** (MIT, 127★, pushed
2026-11-01). Manage the headset from macOS, Windows, Linux or a build-it-yourself iPhone app, over SSH: live view, installs,
files, text, battery and status.

- *Evidence:* publishes a
  [support matrix](https://github.com/saphid/frame-control/blob/main/docs/current-support-matrix.md)
  that separates features tested on a real Frame from those checked only in a VM or by automated
  tests; already documents the SteamOS 0.5.6 beta's connection changes.
- *Alternatives:* [Frame Connect](https://github.com/DevctioN/FrameConnect) (MIT, Windows only);
  [FrameMate](https://github.com/nailuj05/framemate) (GPL-3.0, 121★) for a phone companion with
  mirroring and notifications.

**Tweaks and configuration**

- [Frame Tweaks](https://github.com/AstronautCheetah/frame-tweaks) (MIT): a checklist of desktop-mode
  fixes and add-ons, each removable. Tested on SteamOS 0.4.5 on one headset; no telemetry, per its
  README.
- [steam-frame-nix](https://github.com/lhns/steam-frame-nix) (Apache-2.0): Nix Home Manager modules,
  for people who want the whole setup declarative. It lists every change it makes outside Nix and
  has a cleanup command that removes them.

**Plugin loader: [Framey](https://github.com/chaosfox26/framey)** (GPL-2.0), a Decky-style loader with
a panel in Steam's bottom bar, installed by the [Framey App](https://github.com/chaosfox26/framey-app).
Tested on SteamOS 0.4.5 beta; its README notes a Steam update can break it. Its first plugin is fan
control.

**Keeping apps updated:** [Frametanium](https://github.com/Cogential/frametanium) installs and updates
Frame apps from GitHub releases and discovers new ones. *No licence file.*

**Development**

- **Valve's Steam Runtime 4 arm64 SDK** is public (container image
  `registry.gitlab.steamos.cloud/steamrt/steamrt4/sdk/arm64`, sysroot tarballs on
  [repo.steampowered.com](https://repo.steampowered.com/steamrt4/images/latest-public-stable/)).
  WiVRn's CI builds its Frame client in it, which makes it a working reference.
- Valve's [frame-developer-tools](https://gitlab.steamos.cloud/frame-public/frame-developer-tools)
  (perfetto, gpuvis, gfxreconstruct and gamescope helpers) and the
  [debugging guide](https://partner.steamgames.com/doc/steamhardware/steamframe/debugging).
- [steam-frame-harness](https://github.com/JonahSimon/steam-frame-harness) (MIT): drives a PC-streamed
  Frame with nobody wearing it, for automated game testing. New (2026-10-31); patches SteamVR internals,
  so expect breakage on updates.
- [frame-commons/catalog](https://github.com/frame-commons/catalog) (**maintained by this org's
  admin**): the catalog data as `catalog.json` for installers and launchers to read, and the
  `steam-frame.yml` manifest checker.

## Hardware

**Open hardware is early:** a printable mount, a camera-module scan, and some PCB designs still in
progress.

- [steam-frame-pd100-mount](https://github.com/DeeJanuz/steam-frame-pd100-mount) (MIT): 3D-printable
  mounts for a BoboVR PD100 battery dock on the rear pod.
- [Frame Workshop](https://github.com/Nieko27/Frame-Workshop) (CERN-OHL-S-2.0, 89★): open designs
  in progress, such as a face tracker and a general-purpose radio dongle. Its README marks them R&D
  or work in progress.
- [3dscan-ArcturusCamera](https://github.com/ravngr/3dscan-ArcturusCamera) (CC-BY-SA-4.0): a 3D scan
  of the Arcturus colour camera module, useful for designing around it.

[awesome-steam-frame](https://github.com/kosantosbik/awesome-steam-frame) covers commercial
accessories and hardware more widely.

## Gaps

Areas where we found no good open answer, in case you are looking for something to build:

- A hand tracker that runs on the Frame at a CPU cost people will accept.
- A local video player built for the headset.
- A record of which community tools still work after each headset update. [COMPAT.md](COMPAT.md) is
  meant to be that, and it fills only as projects add `tested:` records.
- Independent test reports for anything Mac-hosted.

---

Part of [frame-commons](https://github.com/frame-commons). Not affiliated with Valve. "Steam" and
"Valve" are Valve's trademarks. This guide is CC0, like the catalog data: copy it into anything.
