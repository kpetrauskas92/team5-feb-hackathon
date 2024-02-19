/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Global templates in root
    "./**/templates/**/*.html", // Templates in each app
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: [
      {
        valentine: {
          ...require("daisyui/src/theming/themes")["light"],
          "primary": "#5c2f3b",
          "secondary": "#a24c6f",
          "base-100": "#f6e7f3",
          "info": "#5c2f3b",
        },
      },
      {
        mytheme: {
          "primary": "#f6e7f3",
          "secondary": "#a24c6f",
          "accent": "#78afb2",
          "neutral": "#ffffff",
          "base-100": "#5c2f3b",
          "info": "#5c2f3b",
        },
      },
    ],
    darkTheme: "mytheme", // name of one of the included themes for dark mode
    base: true, // applies background color and foreground color for root element by default
    styled: true, // include daisyUI colors and design decisions for all components
    utils: true, // adds responsive and modifier utility classes
    prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colors)
    logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
    themeRoot: ":root", // The element that receives theme color CSS variables
  },
};

