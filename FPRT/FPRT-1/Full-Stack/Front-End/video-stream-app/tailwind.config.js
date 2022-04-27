module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        yt: {
          100: "hsl(0,0%,12%)",
          200: "hsl(0,0%,9%)",
        },
        yt_red: "hsl(0,100%,50%)",
        hover: "rgba(255,255,225,0.1)",
      },
    },
  },
  plugins: [require("@tailwindcss/line-clamp")],
};
