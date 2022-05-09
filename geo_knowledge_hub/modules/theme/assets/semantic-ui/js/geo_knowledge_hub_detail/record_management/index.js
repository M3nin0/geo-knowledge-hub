// This file is part of InvenioRDM
// Copyright (C) 2020-2021 CERN.
// Copyright (C) 2020-2021 Northwestern University.
// Copyright (C) 2021 Graz University of Technology.
//
// Invenio RDM Records is free software; you can redistribute it and/or modify it
// under the terms of the MIT License; see LICENSE file for more details.

import React from "react";
import ReactDOM from "react-dom";

import { RecordManagement } from "./components/RecordManagement";

const recordManagementCustomAppDiv = document.getElementById(
  "recordManagementCustom"
);

if (recordManagementCustomAppDiv) {
  ReactDOM.render(
    <RecordManagement
      record={JSON.parse(recordManagementCustomAppDiv.dataset.record)}
      permissions={JSON.parse(recordManagementCustomAppDiv.dataset.permissions)}
    />,
    recordManagementCustomAppDiv
  );
}
