#version 330 core
out vec4 gl_FragColor;

#ifdef GL_ES
precision highp float;
#endif

#extension GL_OES_standard_derivatives : enable

uniform vec2 resolution;   // Screen (Viewport) resolution.
uniform vec2 surfaceSize;  // surfaceSize is equal to: vec2(resolution.x / resolution.y, 1.0)
uniform float time;        // shader runtime
uniform vec2 mouse;        // Normalized mouse position. value range [0.0 - 1.0]

void main( void ) {
	vec2 position = (gl_FragCoord.xy / resolution.xy) + mouse / 4.0;

	float color = 0.0;
	color += sin(position.x * cos(time / 15.0) * 80.0) + cos(position.y * cos(time / 15.0) * 10.0);
	color += sin(position.y * sin(time / 10.0) * 40.0) + cos(position.x * sin(time / 25.0) * 40.0);
	color += sin(position.x * sin(time / 5.0) * 10.0) + sin(position.y * sin(time / 35.0) * 80.0);
	color *= sin(time / 10.0) * 0.5;

	gl_FragColor = vec4(vec3(color, color * 0.5, sin(color + time / 3.0) * 0.75), 1.0);
}
