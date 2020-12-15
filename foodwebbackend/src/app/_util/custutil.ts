export function isNullOrUndefined(value: any) {
  return value === null || value === undefined;
}
export function isBoolean(value: any) {
  return typeof value === 'boolean'
}
export const shallowEqual = (object, compareObject) => {
  try {
    const keys = Object.keys(object);

    const compareKeys = Object.keys(compareObject);

    if (keys.length !== compareKeys.length) {
      return false;
    }

    return keys.every((key) => {
      if (!object[key] && !compareObject[key]) {
        return true;
      }
      if (typeof object[key] === 'object') {
        return shallowEqual(object[key], compareObject[key]);
      } else if (object[key] !== compareObject[key]) {
        return false;
      }
      return true;
    });
  } catch (err) {
    console.error(err);
  }
};
