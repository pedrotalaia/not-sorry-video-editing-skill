# Reusable short-form video editing rules

Use this file as the default brief for Instagram Reels and TikTok shorts in the current project. The user's instructions and project-specific brief take priority. Preserve approved choices across revisions unless the user asks to change them.

## 1. Project setup

- Read this file, applicable `AGENTS.md` or `CLAUDE.md` instructions, and any project brief before starting.
- Inspect `sources/`, `assets/`, and `references/`. Read reference documents and review the actual example videos when accessible.
- Keep original media and filenames intact. Put derived media in `work/`, transcripts in `transcripts/`, edit files in `compositions/`, and deliverables in `exports/`. Create these folders as needed.
- Choose suitable tools and libraries for the job. The user does not need to prescribe them. If a particular editor is requested, deliver a compatible editable project where supported.
- Make reasonable creative and technical decisions. Ask only for information that materially affects the result and cannot be inferred from the footage, brief, or references.

## 2. Review the footage before editing

- Inspect every relevant source for duration, resolution, frame rate, orientation, pixel aspect ratio, audio channels, and recording quality.
- Review the footage and speech across the recording. A contact sheet alone is insufficient to assess delivery, sound, timing, or the quality of cuts.
- Transcribe spoken content when useful. Check the spoken language, names, terminology, and timestamps. Distinguish setup chatter, false starts, repeated takes, and production notes from usable material.
- Identify the strongest hooks, useful explanations, examples, stories, and conclusions. Note missing context, screen recordings, or other supporting material.
- Check for room echo, noise, clipping, unequal microphones, and audio/video delay before choosing an audio treatment.

## 3. Recommend the number of clips and propose a storyboard

Start with a concise assessment of how many worthwhile, self-contained Reels or shorts the footage supports. Base the count on distinct ideas and complete payoffs, rather than a fixed quota. Recommend fewer strong clips when the material does not support more.

For each proposed clip, provide:

| Field | Include |
| --- | --- |
| Clip ID and priority | Recommended production and publishing order |
| Working title and angle | The main idea and why it is useful to the intended audience |
| Opening hook | A strong opening supported by the recorded content |
| Source selections | Filenames and approximate source in/out timestamps, measured from file start |
| Estimated duration | Usually 30–60 seconds; use the length the idea needs and flag exceptions |
| Story beats | Hook, context, explanation or example, payoff, and a suitable closing |
| Visual treatment | Framing, title, captions, graphics, B-roll, and planned zooms |
| Assets and gaps | Available assets, proposed additions, and missing material that matters |

Explain whether the same edit suits both platforms or whether a platform-specific version would help. Identify optional clips separately from the recommended set, and avoid near-duplicate clips without a clear purpose.

Present the recommendation before full editing and retain the storyboard in `compositions/`. If the user requests only a proposal, deliver the proposal. If the user asks for finished videos, proceed with the recommended plan unless they explicitly request a review before editing. Do not add routine approval gates.

## 4. References, assets, and creative freedom

- Look in both `references/` and `assets/` for videos, logos, fonts, music, images, documents, and prior approved exports. Follow any supplied notes about what to borrow from each reference.
- Translate references into concrete choices: typography, title scale, pacing, graphic layout, framing, transitions, caption placement, and sound treatment.
- If references or assets are missing, create a coherent visual direction that fits the speaker, subject, and intended audience. Keep it readable, purposeful, and consistent.
- Create simple original diagrams, text treatments, and illustrations when they clarify the spoken explanation. Use external or generated assets only when useful, with suitable usage rights; record their provenance.
- Never invent performance results, testimonials, screenshots, statistics, quotations, or offers. Do not imply a diagram is an actual product screenshot or that illustrative results are real.
- Do not copy another creator's branding, footage, or music merely because it appears in a reference.
- If a reference is inaccessible, say so and continue with accessible material. Do not claim to have reviewed it.

## 5. Story and pacing

- Open promptly with the strongest relevant hook. Remove dead air, setup chatter, repeated wording, and unnecessary detours while preserving meaning and a natural delivery.
- Make every clip understandable on its own. Keep the context needed to support its conclusion.
- Preserve the speaker's meaning and voice. Do not splice statements into claims the speaker did not make or make captions say something different from the speech.
- Prefer a complete useful explanation over an arbitrary runtime. Avoid cutting words, breaths, or sentences abruptly to meet a target.
- Close with the recorded payoff or a relevant call to action. Do not invent a promised resource, commercial offer, or engagement incentive.

## 6. Framing, titles, graphics, and branding

- Default to a vertical 9:16 composition at 1080 × 1920. Preserve the source cadence when practical; use a different frame rate only for a clear reason.
- Establish a comfortable baseline showing the head, shoulders, and useful gestures. Reframe deliberately from landscape footage; do not stretch the person to fill the canvas.
- Use selective punch-ins and gentle pushes to emphasize important lines. Set zoom limits relative to the baseline crop so multiple crops and zooms do not compound into an excessively tight shot.
- Keep the head inside the frame throughout movement. Protect useful gestures and leave room for titles, captions, and platform overlays.
- For speaker-plus-diagram layouts, zoom the speaker independently so diagrams and text remain stable and readable.
- Use a large, readable opening title inspired by the references. A title behind the head is a preferred depth effect when appropriate: use a moving foreground mask and inspect its edges throughout the shot. Keep enough of the title visible to read it.
- Place a supplied signature or logo at the bottom right by default, with sufficient inset, contrast, and space from platform controls and captions. Keep branding consistent across clips.
- Keep graphics simple and faithful to the explanation. Check legibility at phone size, not just at full resolution.

## 7. Captions

- Caption in the spoken language unless the user requests translation. Use accurate wording, punctuation, names, and technical terms.
- Use short, meaningful phrases. Avoid splitting phrases awkwardly or combining the end of one sentence with the start of another merely to fill a caption.
- Align captions to the actual final edit. Recheck timings after any cut, speed, or audio-timing change.
- Use readable type and sufficient contrast. Keep captions away from the face, key graphics, branding, and platform interface areas.
- Deliver burned-in captions plus a separate `.srt` file unless the user requests another approach.

## 8. Audio

- Start from the best available original microphone channel. Check channels before mixing; do not combine a clean microphone with a poorer room recording unnecessarily.
- Reduce distracting echo, room noise, and rumble while retaining natural speech and consonants. Use gentle processing and avoid metallic artifacts, pumping, abrupt gates, or exaggerated loudness.
- Compare processing at similar playback levels so louder is not mistaken for better. Listen to pauses, breaths, word endings, and transitions as well as loud speech.
- Prevent new clipping and keep sensible peak headroom. Aim for consistent speech loudness across clips; measure the finished export rather than assuming a normalization setting guarantees the target.
- Add music or effects only when they support the intended style. Keep speech intelligible and use suitable assets; speech-only is acceptable.
- For picture-only revisions, preserve the latest approved cleaned audio and its timing. For audio-only revisions, preserve the approved picture edit.

## 9. Export and verification

Default delivery: MP4, H.264 video, AAC audio, 1080 × 1920, square pixels, and correct 9:16 display geometry. Use web-friendly playback settings and numbered exports such as `topic-reel-01-v01.mp4`.

Before delivering:

- Confirm stored dimensions **and** playback geometry: sample aspect ratio **1:1**, display aspect ratio **9:16**, and no unintended rotation or crop metadata. Check the encoded stream and frames, especially after stacking, padding, scaling, zooming, or concatenating clips. Dimensions alone are not sufficient.
- Explicitly reset pixel aspect ratio after transformations that can change it, and in the final composition. Do not rely on inherited metadata from an intermediate layer.
- Decode the full final export and check for errors, unexpected black frames, freezes, missing media, and incorrect duration.
- Review playback across the complete edit, including every cut and zoom. Inspect the first and last frames, the tightest framing, moving title masks, caption placement, diagrams, and logo position.
- Listen to the exported audio for echo-reduction artifacts, clipping, intelligibility, abrupt transitions, and synchronization. Check measured loudness and peaks.
- Confirm captions match the exported speech and that source cuts do not truncate words or change meaning.
- After revisions, check the changed parts and any affected transitions. Verify that approved audio or picture remained unchanged when applicable.
- Record what was actually checked. If playback or listening is unavailable, state that limitation rather than claiming a complete audiovisual review.
- Fix observed problems before delivery. Do not label an export as verified merely because rendering completed.

## 10. Delivery and reusable project records

- Provide clear links to the finished videos and subtitle files. Include a cover image when useful or requested.
- Briefly summarize the chosen clips, meaningful editing choices, and any material source limitations.
- Keep the storyboard, source timestamps, export settings, asset provenance, and reproducible edit instructions or editable project files in `compositions/`.
- Preserve earlier exports for comparison. Make new revisions separately and identify the recommended latest version clearly.
- Creating an export does not authorize publishing. Publish or send videos externally only when the user requests it.

## Example starting prompt

> Read `editing-rules.md`, review the footage in `sources/`, and check `assets/` and `references/`. Recommend how many strong Instagram Reels or TikTok shorts the material supports and propose a storyboard for each. Then create the recommended edits using these rules. Choose suitable tools, preserve the originals, and verify the finished exports before delivery.

For a storyboard-only task, end the prompt with: **“Propose the clips and storyboards first; do not render yet.”**
