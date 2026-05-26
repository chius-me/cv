export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const country = request.cf?.country;

    if (url.pathname === "/" || url.pathname === "/zh/" || url.pathname === "/zh") {
      const isChina = country === "CN";
      const target = isChina
        ? "/zh/Yao_Chius_CV.pdf"
        : "/Yao_Chius_CV.pdf";
      return Response.redirect(new URL(target, request.url), 302);
    }

    return env.ASSETS.fetch(request);
  },
};
