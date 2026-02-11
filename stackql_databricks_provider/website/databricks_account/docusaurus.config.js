// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

// Provider configuration - change these for different providers
const providerName = "awscc"; // used in URLs and file paths, must be all lowercase
const providerTitle = "AWS Cloud Control";

const providerDropDownListItems = [
  {
    label: 'AWS',
    to: '/providers/aws',
  },
  {
    label: 'Azure',
    to: '/providers/azure',
  },
  {
    label: 'Google',
    to: '/providers/google',
  },
  {
    label: 'Databricks',
    to: '/providers/databricks',
  },
  {
    label: 'Snowflake',
    to: '/providers/snowflake',
  },
  {
    label: 'Confluent',
    to: '/providers/confluent',
  },
  {
    label: 'Okta',
    to: '/providers/okta',
  },
  {
    label: 'GitHub',
    to: '/providers/github',
  },
  {
    label: 'OpenAI',
    to: '/providers/openai',
  },
  {
    label: '... More',
    to: '/providers',
  },
];

const footerStackQLItems = [
  {
    label: 'Documentation',
    to: '/stackqldocs',
  },
  {
    label: 'Install',
    to: '/install',
  },
  {
    label: 'Contact us',
    to: '/contact-us',
  },
];

const footerMoreItems = [
  {
    label: 'Providers',
    to: '/providers',
  },
  {
    label: 'stackql-deploy',
    to: '/stackql-deploy',
  },            
  {
    label: 'Blog',
    to: '/blog',
  },
  {
    label: 'Tutorials',
    to: '/tutorials',
  },            
];

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: `StackQL ${providerTitle} Provider`,
  tagline: `Query and Provision ${providerTitle} Resources using StackQL`,
  favicon: 'img/favicon.ico',
  staticDirectories: ['static'],
  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: `https://${providerName}-provider.stackql.io`,
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'stackql', // Usually your GitHub org/user name.
  projectName: `stackql-provider-${providerName}`, // Usually your repo name.

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          // editUrl: 'https://github.com/stackql/stackql-deploy/tree/main/website/',
          routeBasePath: '/', // Set the docs to be the root of the site
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      // Replace with your project's social card
      image: 'img/stackql-cover.png',
      navbar: {
        logo: {
          alt: 'StackQL Registry',
          href: '/providers',
          src: 'img/stackql-registry-logo.svg',
          srcDark: 'img/stackql-registry-logo-white.svg',
        },
        items: [
          {
            to: '/install',
            position: 'left',
            label: 'Install',
          },
          {
            to: '/stackql-deploy',
            position: 'left',
            label: 'stackql-deploy',
          },
          {
            to: '/providers',
            type: 'dropdown',
            label: 'Providers',
            position: 'left',
            items: providerDropDownListItems,
          },
          {
            type: 'dropdown',
            label: 'More',
            position: 'left',
            items: [
              {
                to: '/stackqldocs',
                label: 'StackQL Docs',
              },
              {
                to: '/blog',
                label: 'Blog',
              },
              {
                to: '/tutorials',
                label: 'Tutorials',
              },
            ],
          },
          {
            href: 'https://github.com/stackql/stackql',
            position: 'right',
            className: 'header-github-link',
            'aria-label': 'GitHub repository',
          },          
        ],
      },
      footer: {
        style: 'dark',
        logo: {
          alt: 'StackQL',
          href: '/providers',
          src: 'img/stackql-registry-logo.svg',
          srcDark: 'img/stackql-registry-logo-white.svg',
        },
        links: [
          {
            title: 'StackQL',
            items: footerStackQLItems,
          },
          {
            title: 'More',
            items: footerMoreItems,
          },
        ],
        copyright: `© ${new Date().getFullYear()} StackQL Studios`,
      },
      colorMode: {
        // using user system preferences, instead of the hardcoded defaultMode
        respectPrefersColorScheme: true,
      },
      prism: {
        theme: prismThemes.nightOwl,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
