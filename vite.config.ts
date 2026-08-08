import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

// Minimal declaration so we can read an env override without pulling in @types/node.
declare const process: { env: Record<string, string | undefined> };

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    // C: is space-constrained on this machine, so emit the bundle to D:.
    // Override with VITE_OUT_DIR for normal deployments.
    outDir: process.env.VITE_OUT_DIR || 'D:/portfolio-build/dist',
    emptyOutDir: true,
    sourcemap: false,
    chunkSizeWarningLimit: 1000,
  },
});
