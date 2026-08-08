/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        paper: '#f2eee4',
        'paper-2': '#eae3d3',
        card: '#faf8f2',
        ink: '#17130d',
        'ink-soft': '#463f31',
        muted: '#867c69',
        accent: '#dd3a1b',
        'accent-deep': '#b32c11',
        line: '#17130d',
      },
      fontFamily: {
        display: ['Fraunces', 'Georgia', 'serif'],
        sans: ['Archivo', 'system-ui', 'sans-serif'],
        mono: ['"Space Mono"', 'ui-monospace', 'monospace'],
      },
      keyframes: {
        ticker: {
          from: { transform: 'translateX(0)' },
          to: { transform: 'translateX(-50%)' },
        },
      },
      animation: {
        ticker: 'ticker 30s linear infinite',
      },
    },
  },
  plugins: [],
};
