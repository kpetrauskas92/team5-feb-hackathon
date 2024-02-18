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
      "valentine",
      {
        mytheme: {
          "primary": "#f637f3",
          "secondary": "#a24c6f",
          "accent": "#78afb2",
          "neutral": "#ffffff",
          "base-100": "#5c2f3b",
        },
      },
      true
    ],
    // themes: true, // false: only light + dark | true: all themes | array: specific themes like this ["light", "dark", "cupcake"]
    darkTheme: "mytheme", // name of one of the included themes for dark mode
    base: true, // applies background color and foreground color for root element by default
    styled: true, // include daisyUI colors and design decisions for all components
    utils: true, // adds responsive and modifier utility classes
    prefix: "", // prefix for daisyUI classnames (components, modifiers and responsive class names. Not colors)
    logs: true, // Shows info about daisyUI version and used config in the console when building your CSS
    themeRoot: ":root", // The element that receives theme color CSS variables
  },
};

// #f637f3 = light pink 
// #a24c6f = plum
// #5c2f3b = brown 
// #a592f0 = lavendar
// #78afb2 = green 
