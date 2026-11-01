# `steam-frame.yml` — a project manifest for Steam Frame software

Version 0 (draft). Status: open for comment.

A small file at the root of a repository that says what the project does for the
Steam Frame, in a form a program can read. The frame-commons catalog reads it every
week, and so can any installer, launcher or list that wants to.

Carrying the file does not make a project part of frame-commons or bind it to anything.
It only describes the project.

## Why another file

GitHub already knows a repository's name, description, licence, stars and last push, so
the manifest repeats none of that. What GitHub cannot know is:

- which pieces of the headset the project provides (hands, camera access, a desktop...),
- which interfaces it implements, so other projects can build on it,
- where it runs (on the headset, on a PC, or both),
- how to install it, and
- **which SteamOS and SteamVR versions it has been tested on.** Headset updates break
  community software often, and today the only record is prose in each README.

Existing formats were considered first: publiccode.yml (right idea, far too heavy),
AppStream metainfo (install-time XML, no "tested on"), codemeta.json (free-text fields, no
test reports), Decky's and Framey's `plugin.json` (loader metadata, and the name is taken).
Field meanings follow codemeta where one exists, so the catalog can publish codemeta for
anyone who wants it.

## The file

```yaml
manifest: 0
provides: [hands, camera]
implements:
  - openxr:XR_EXT_hand_tracking
  - shm:fh_hands@1
runs_on: headset
install: https://example.org/install.md
tested:
  - { steamos: "0.4.5", build: "20261007", steamvr: "2.18.2", channel: beta, date: 2026-10-20, result: works }
```

Only `provides` is required. A two-line file is a complete manifest:

```yaml
manifest: 0
provides: [voice, input]
```

## Keys

| Key | Required | Type | Meaning |
|---|---|---|---|
| `manifest` | recommended | integer | Schema version. `0` for this draft. Assumed `0` when absent. |
| `provides` | **yes** | list of terms | What the project gives a Frame user, from the vocabulary below. One or more. |
| `implements` | no | list of strings | Interfaces others can build on, as `kind:name`, optionally `@version`. See below. |
| `runs_on` | no | `headset` \| `pc` \| `both` | Where the project's own code runs. |
| `install` | no | string | One shell command, or a URL to install instructions. |
| `tested` | no | list of test records | One record per test. Add a line; don't edit old ones. |

### `provides` vocabulary

| Term | For projects that... |
|---|---|
| `camera` | read the headset's cameras (tracking, eye, colour) and hand frames to others |
| `hands` | track hands or turn hand data into input |
| `eyes` | track or use gaze, eyelids, pupils |
| `face` | track mouth or face expressions |
| `passthrough` | show or control the camera view of the room |
| `streaming` | move video or apps between the headset and other machines |
| `input` | add or remap input: controllers, keyboards, mice, gestures |
| `voice` | speech to text, voice commands |
| `desktop` | windows, desktops and launchers in VR |
| `overlay` | HUDs, panels, performance or status overlays |
| `media` | play video, audio or other media |
| `tooling` | installers, managers, development and test tools |
| `compat-fix` | fixes and shims that make other software run |
| `game` | games and ports |
| `hardware` | mounts, mods and hardware designs |

New terms are added by pull request to this file. Unknown terms are rejected by the
checker so the catalog's sections stay meaningful.

### `implements`

Free strings of the form `kind:name[@version]`. Kinds in use:

| Kind | Example | Meaning |
|---|---|---|
| `openxr` | `openxr:XR_EXT_hand_tracking` | An OpenXR extension the project provides (as a runtime or API layer). |
| `shm` | `shm:fh_hands@1` | A shared-memory interface, by its spec name and version. |
| `osc` | `osc:vrchat-eye` | An OSC address family. |
| `openvr` | `openvr:driver` | An OpenVR / SteamVR driver or overlay. |
| `vrcft` | `vrcft:module` | A VRCFaceTracking module. |

If you implement an interface someone has published, use its own name so consumers can find
you. For example, `shm:fh_hands@1` is Frametop's hand-data file
([`hands/include/fh_hands.h`](https://github.com/Frametop/frametop/blob/main/hands/include/fh_hands.h)).

### Test records

| Field | Required | Example | Meaning |
|---|---|---|---|
| `steamos` | yes | `"0.4.5"` | The **headset's** SteamOS version (its own 0.x line, not the desktop 3.x one). |
| `build` | recommended | `"20261007"` | The headset OS build ID, from Settings → System. |
| `steamvr` | recommended | `"2.18.2"` | SteamVR version. |
| `channel` | recommended | `stable` \| `beta` \| `preview` | The update channel the headset was on. |
| `date` | yes | `2026-10-20` | When you tested. |
| `result` | yes | `works` \| `partial` \| `broken` | What happened. |
| `notes` | no | `"gaze ok, blink lags"` | One short line. |

**Quote version strings.** YAML reads `2.18` as a number and drops the trailing zero from
`2.10`. The checker rejects unquoted versions for that reason.

A `broken` record is as useful as a `works` one: it is how other users learn an update
broke something before they install it.

## Checking a manifest

```sh
pipx run --spec git+https://github.com/frame-commons/catalog fc-catalog check steam-frame.yml
```

or, from a checkout of the catalog, `bin/fc-catalog check path/to/steam-frame.yml`.

## Compatibility

- Readers must ignore keys they don't know, so later versions can add keys.
- A change that would make an existing valid file invalid bumps `manifest`.

## Licence

This specification is CC0 1.0 ([LICENSE](LICENSE)): copy it, change it, use it anywhere.
