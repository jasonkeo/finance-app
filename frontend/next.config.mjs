/** @type {import('next').NextConfig} */
const nextConfig = {
    // skipTrailingSlashRedirect: true,
    // trailingSlash: true,
    output: 'export',
    webpackDevMiddleware: config => {
        config.watchOptions = {
            poll: 800,
            aggregateTimeout: 300,
        };
        return config;
    },
    reactStrictMode: true,
  // Suppress build warnings
  typescript: {
    ignoreBuildErrors: true,
  },
  eslint: {
    ignoreDuringBuilds: true,
  },
};

export default nextConfig;