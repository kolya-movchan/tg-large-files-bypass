function generatePromptDeeplink(promptText: string): string {
  const url = new URL("cursor://anysphere.cursor-deeplink/prompt");
  url.searchParams.set("text", promptText);
  return url.toString();
}
const deeplink = generatePromptDeeplink(
  "Create a React component for user authentication"
);
console.log(deeplink);
