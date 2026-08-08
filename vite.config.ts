import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Minimal declaration so we can read an optional local override without @types/node.
declare const process: { env: Record<string, string | undefined> };

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    // Standard Vite output — Vercel serves this. Set VITE_OUT_DIR only for a
    // local out-of-tree build (e.g. a space-constrained system drive).
    outDir: process.env.VITE_OUT_DIR || 'dist',
    emptyOutDir: true,
    sourcemap: false,
    chunkSizeWarningLimit: 1000,
  },
});
