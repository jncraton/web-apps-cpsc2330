---
reading: '[MDN: Video and Audio](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_video_and_audio)'
...

# Web Media

## HTML Media Elements

- Web pages often include rich multimedia content
- HTML provides specific elements for audio and video
- These elements embed media directly into your web page

## Video Element

- The `<video>` element embeds a media player for video content
- It offers a standardized way to include visual stories
- This element allows browsers to handle playback directly

## Audio Element

- The `<audio>` element embeds a player for sound content
- It supports background music, podcasts, or sound effects
- This element provides consistent audio experiences on the web

## Source Paths

- The `src` attribute specifies the path to your media file
- This attribute tells the browser where to find the audio or video
- It's essential for the browser to load and play your content

```html
<video src="myvideo.mp4"></video>
<audio src="myaudio.mp3"></audio>
```

## User Controls

- The `controls` attribute adds default playback controls
- These include play/pause, volume, and progress bar
- It gives users immediate interaction with the media

```html
<video src="myvideo.mp4" controls></video>
<audio src="myaudio.mp3" controls></audio>
```

---

Beyond simply displaying media, how might the choice of an `<audio>` or `<video>` element influence user interaction with a page?

## Video Attributes

- Several attributes customize video behavior and appearance
- These provide more control over the user's viewing experience
- They help integrate video seamlessly into your layout

## Autoplay and Loop

- The `autoplay` attribute tries to play media automatically
- The `loop` attribute makes media repeat indefinitely
- Use these cautiously, as they can sometimes annoy users

```html
<video src="intro.mp4" autoplay loop></video>
```

## Muted and Poster

- The `muted` attribute silences the media by default
- The `poster` attribute displays an image before video playback
- A poster can be a placeholder or a preview of the content

```html
<video src="clip.mp4" poster="thumbnail.jpg" controls muted></video>
```

## Exercise

Create a `<video>` element for a short video named `lecture.mp4`. Ensure it has default controls, loops automatically, and displays `cover.jpg` as its poster image. Make sure it's muted by default.

## Multiple Sources

- Different browsers support different media file formats
- You can provide multiple source files for the same media
- This ensures broader compatibility across various user agents

## Source Element

- The `<source>` element specifies alternative media files
- It's placed inside the `<video>` or `<audio>` element
- The browser will pick the first format it understands

```html
<video controls>
  <source src="myvideo.mp4" type="video/mp4">
  <source src="myvideo.webm" type="video/webm">
</video>
```

## Media Type

- The `type` attribute specifies the media's MIME type
- This helps the browser quickly determine compatibility
- It prevents the browser from downloading unsupported files

## Fallback Content

- Include text or a link for browsers that don't support media
- This content appears if no `<source>` is playable
- It ensures users still get information about the media

```html
<audio controls>
  <source src="mysong.mp3" type="audio/mpeg">
  <p>Your browser does not support audio. Here is a <a href="mysong.mp3">link to the audio file</a>.</p>
</audio>
```

---

How does offering multiple media formats using `<source>` elements improve the accessibility and reach of your web content?

## Web Accessibility

- Media elements must be accessible to all users
- This includes individuals with visual or hearing impairments
- Accessibility is crucial for inclusive web design

## Transcripts and Captions

- Provide transcripts for audio content
- Offer captions for video, including spoken dialogue and sounds
- These help users who cannot hear or who prefer reading

## Track Element

- The `<track>` element specifies timed text tracks for media
- This includes subtitles, captions, and descriptions
- It enhances accessibility and comprehension for many users

```html
<video controls src="myvideo.mp4">
  <track kind="captions" src="captions_en.vtt" srclang="en" label="English">
</video>
```

## Track Kinds

- `kind="captions"` for transcripts of dialogue
- `kind="subtitles"` for translations of dialogue
- `kind="descriptions"` for text descriptions of video actions

## Exercise

Modify the previous `<video>` example (`lecture.mp4`) to include two `<source>` elements: `lecture.mp4` (MP4 format) and `lecture.webm` (WebM format). Also, add a simple paragraph as fallback content for unsupported browsers.

## Audio Descriptions

- For video content, provide audio descriptions for visually impaired users
- These narrate important visual information during pauses in dialogue
- It offers a complete understanding of the video's context

## Best Practices

- Always include `controls` for user autonomy
- Consider `muted` and `autoplay` together for background media
- Optimize media file sizes for faster loading

---

When designing a page with embedded video, what are some of the ethical considerations regarding user experience, especially concerning `autoplay` and `muted` attributes?

## Permissions

- Many user agents prevent autoplay of video and audio

## Exercise

Take the `<video>` element you created earlier and add a `<track>` element. Assume you have a captions file named `lecture_captions.vtt` in English. Give it a suitable label.
