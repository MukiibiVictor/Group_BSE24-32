/*import globals from "globals";
import pluginJs from "@eslint/js";
import tseslint from "typescript-eslint";
//import { ESLintPlugin as tsPlugin, parser as tsParser } from '@typescript-eslint/eslint-plugin';
import tsPlugin from "@typescript-eslint/eslint-plugin";
import tsParser from "@typescript-eslint/parser";

export default [
  {
    files: ["/*.{js,mjs,cjs,ts}"],
    languageOptions: {
      globals: globals.browser,
      ecmaVersion: 2020,
      sourceType: "module",
      parser: tsParser,
    },
    ...pluginJs.configs.recommended,
    ...tseslint.configs.recommended,
    plugins: {
      js: pluginJs,
      "@typescript-eslint": tsPlugin,
    },

    extends: [
      "eslint:recommended",
      "plugin:@typescript-eslint/recommended",
      //"plugin:@typescript-eslint/recommended-requiring-type-checking",
    ],
    env: {
      browser: true,
      es6: true
    },

    parserOptions: {
      ecmaVersion: 2020,
      sourceType: "module"
    },
    rules: {
      "no-unused-vars": "warn",
      "no-console": "off",
      "semi": ["error", "always"],
      "quotes": ["error", "single"]
    }
  }
];


import globals from "globals";
import pluginJs from "@eslint/js";
import tsPlugin from "@typescript-eslint/eslint-plugin";
import tsParser from "@typescript-eslint/parser";
import tseslint from "typescript-eslint";
*/

const globals = require('globals');
const pluginJs = require('@eslint/js');
const tseslint = require('@typescript-eslint/eslint-plugin');
const tsParser = require('@typescript-eslint/parser');
const tsPlugin = require('@typescript-eslint/eslint-plugin');

module.exports = [
  {
    files: ["**/*.{js,mjs,cjs,ts}"],
    languageOptions: {
      globals: {
        ...globals.browser,
        ...globals.es6,
      },
      parser: tsParser, // TypeScript parser
      ecmaVersion: 2020,
      sourceType: "module",
    },
    plugins: {
      js: pluginJs,
      ts: tsPlugin,
      "@typescript-eslint": tsPlugin
    },
    rules: {
      // JavaScript recommended rules
      ...pluginJs.configs.recommended.rules,
      // TypeScript recommended rules
      ...tsPlugin.configs.recommended.rules,

      // Custom rules
      "no-unused-vars": "warn",
      "no-console": "off",
      "semi": ["error", "always"],
      "quotes": ["error", "single"],
      "@typescript-eslint/ban-ts-comment": "error"
    },
  }
];
