#version 330 core

#ifdef GL_ES
precision highp float;
#endif

uniform vec3      iResolution;           // viewport resolution (in pixels)

uniform int       iFrame;                // shader playback frame
uniform float     iTime;                 // shader playback time (in seconds)
uniform float     iTimeDelta;            // render time (in seconds)
uniform vec4      iDate;                 // year, month, day, time in seconds

uniform vec4      iMouse;                // mouse pixel coords. xy: current (if MLB down), zw: click
uniform float     iSampleRate;           // sound sample rate (i.e., 44100)

uniform vec3      iChannelResolution[4]; // channel resolution (in pixels)
uniform float     iChannelTime[4];       // channel playback time (in seconds)

// uniform samplerXX iChannel0..3;          // input channel. XX = 2D/Cube
uniform {channel0_sampler_type} iChannel0;
uniform {channel1_sampler_type} iChannel1;
uniform {channel2_sampler_type} iChannel2;
uniform {channel3_sampler_type} iChannel3;

out vec4 glFragColor;

{shader_toy_body}

void main(void) {{
    glFragColor.a = 1.;
    mainImage(glFragColor, gl_FragCoord.xy);
}}
