// Copyright (C) 2025 Intel Corporation
// SPDX-License-Identifier: Apache-2.0

import { Injectable } from '@nestjs/common';
import { FEATURE_STATE, Features } from './features.model';
import { ConfigService } from '@nestjs/config';

@Injectable()
export class FeaturesService {
  features: Features = {
    summary: FEATURE_STATE.OFF,
    search: FEATURE_STATE.OFF,
  };

  constructor(private $config: ConfigService) {
    this.features.summary =
      this.$config.get<FEATURE_STATE>('features.summary')!;
    this.features.search = this.$config.get<FEATURE_STATE>('features.search')!;
  }

  getFeatures(): Features {
    return this.features;
  }

  hasFeature(feature: keyof Features): boolean {
    return this.features[feature] === FEATURE_STATE.ON;
  }
}
