/*
 * This file is part of GEO Knowledge Hub.
 * Copyright (C) 2021-2022 GEO Secretariat.
 *
 * GEO Knowledge Hub is free software; you can redistribute it and/or modify it
 * under the terms of the MIT License; see LICENSE file for more details.
 */

import _get from "lodash/get";

/**
 * Extract a GEO Work Programme Activity Name from a String
 *
 * @param {string} programmeActivityName String containing the Programme Name
 */
export const extractProgrammeActivityAcronym = (programmeActivityName) =>
  programmeActivityName
    ? _get(programmeActivityName.match(/\(([^)]+)\)/), 1, null)
    : null;

/**
 * Generate record links based on parent type.
 *
 * @param {string} recordId Record Identifier (PID)
 * @param {string} recordType Record type (e.g., package, resource)
 * @returns {object} Object with the links created.
 */
export const recordTypeLinksFactory = (recordId, recordType) => {
  const recordLinks = {
    package: {
      published: {
        api: `/api/packages/${recordId}`,
        ui: `/packages/${recordId}`,
      },
      draft: {
        api: `/api/packages/${recordId}/draft`,
        ui: `/uploads/packages/${recordId}`,
      },
    },
    resource: {
      published: {
        api: `/api/records/${recordId}`,
        ui: `/records/${recordId}`,
      },
      draft: {
        api: `/api/records/${recordId}/draft`,
        ui: `/uploads/${recordId}`,
      },
    },
  };

  return recordLinks[recordType];
};
