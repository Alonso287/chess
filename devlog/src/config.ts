export const SITE = {
  website: "https://chesslabs.vercel.app/", // replace this with your deployed domain
  author: "Alonso Navarro",
  profile: "https://github.com/Alonso287",
  desc: "Mi Devlog de desarrollo de ChessLabs, donde iré actualizando mi progreso con el motor de ajedrez.",
  title: "ChessLabs",
  ogImage: "",
  lightAndDarkMode: true,
  postPerIndex: 4,
  postPerPage: 4,
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
  showArchives: false,
  showBackButton: true, // show back button in post detail
  editPost: {
    enabled: false,
    text: "Sugerir cambios",
    url: "https://github.com/Alonso287/chess/edit/main/",
  },
  showTags: false,
  dynamicOgImage: true,
  dir: "ltr", // "rtl" | "auto"
  lang: "es", // html lang code. Set this empty and default will be "en"
  timezone: "Europe/Madrid", // Default global timezone (IANA format) https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
} as const;
