// Reads service configuration. Uses js-yaml's safe loader only, never yaml.load.
import yaml from "js-yaml";
import { readFileSync } from "fs";

export function loadConfig(path: string): Record<string, unknown> {
  return yaml.safeLoad(readFileSync(path, "utf8")) as Record<string, unknown>;
}
